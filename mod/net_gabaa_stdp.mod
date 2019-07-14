INDEPENDENT {t FROM 0 TO 1 WITH 1 (ms)}

NEURON {
	POINT_PROCESS NET_GABAa_STDP
	RANGE C, R, R0, R1, g, gmax, lastrelease, TimeCount, Erev, Alpha, Beta, Cdur, Cmax,
              tau, e, i, d, p, dtau, ptau, verbose, learning, LR, maxWeight, minWeight, 
              forSpike, tmp, forDA   
	NONSPECIFIC_CURRENT i
	GLOBAL Prethresh, Deadtime, Rinf, Rtau
}

UNITS {
	(nA) = (nanoamp)
	(mV) = (millivolt)
	(umho) = (micromho)
	(mM) = (milli/liter)
}

PARAMETER {
	tau = 0.1 (ms) <1e-9,1e9>:tau = 0.1 (ms) <1e-9,1e9>
	e = 0	(mV)
	d = 1 <0,1>: depression factor (multiplicative to prevent < 0)
	p = 1 : potentiation factor (additive, non-saturating)
	dtau = 34 (ms) : 34 depression effectiveness time constant
	ptau = 17 (ms) : 17 Bi & Poo (1998, 2001)
	verbose = 0
	learning = 1
	LR = 1
	maxWeight = 1
	minWeight = 0
	forSpike = 0 : use to judge whether it fires or not.
	tmp = 0
	forDA = 0.02

	dt		(ms)
	Cmax	= 1	(mM)		: max transmitter concentration
	Cdur	= 1	(ms)		: transmitter duration (rising phase)
	Alpha	= 5	(/ms mM)	: forward (binding) rate
	Beta	= 0.18	(/ms)		: backward (unbinding) rate
	Erev	= -80	(mV)		: reversal potential
	Prethresh = 0 			: voltage level nec for release
	Deadtime = 1	(ms)		: mimimum time between release events
}

ASSIGNED {
	v		(mV)		: postsynaptic voltage
	i 		(nA)		: current = g*(v - Erev)
	g 		(umho)		: conductance
	C		(mM)		: transmitter concentration
	R				: fraction of open channels
	R0				: open channels at start of release
	R1				: open channels at end of release
	Rinf				: steady state channels open
	Rtau		(ms)		: time constant of channel binding
	pre 				: pointer to presynaptic variable
	lastrelease	(ms)		: time of last spike
	TimeCount	(ms)		: time counter
	
	flg

	tpost (ms)
	gmax		(umho)		: maximum conductance

	
    }
    :VERBATIM
    :int counter = 0;
    :ENDVERBATIM

INITIAL {
	R = 0
	C = 0
	Rinf = Cmax*Alpha / (Cmax*Alpha + Beta)
	Rtau = 1 / ((Alpha * Cmax) + Beta)
	lastrelease = -1000
	R1=0
	TimeCount=-1
	
	flg = 0

	tpost = -1e9
	net_send(0, 1)
}

BREAKPOINT {
	:VERBATIM
	:printf("BREAKPOINT\t%d\t%f\n",counter++, t);
	:ENDVERBATIM

	SOLVE release
	g = gmax * R
	i = g*(v - Erev)
}

PROCEDURE release() {
	:VERBATIM
	:printf("release\t\t%d\t%f\n",counter++, t);
	:ENDVERBATIM

	:will crash if user hasn't set pre with the connect statement 

	TimeCount=TimeCount-dt			: time since last release ended
	
	: ready for another release?
	if (TimeCount < -Deadtime) {
	    if (flg > 0){		: spike occured?
		C = Cmax			: start new release
		R0 = R
		lastrelease = t
		TimeCount=Cdur
		flg = 0
	    }
	}else if (TimeCount > 0) {		: still releasing?
	    : do nothing
	} else if (C == Cmax) {			: in dead time after release
	    R1 = R
	    C = 0.
	}

	if (C > 0) {				: transmitter being released?

	   R = Rinf + (R0 - Rinf) * exptable (- (t - lastrelease) / Rtau)
				
	} else {				: no release occuring

  	   R = R1 * exptable (- Beta * (t - (lastrelease + Cdur)))
	}

	VERBATIM
	return 0;
	ENDVERBATIM
}

FUNCTION exptable(x) { 
	TABLE  FROM -10 TO 10 WITH 2000

	if ((x > -10) && (x < 10)) {
		exptable = exp(x)
	} else {
		exptable = 0.
	    }
	}
}

NET_RECEIVE(w (uS), tpre (ms)) {
    flg = 1
    INITIAL { tpre = -1e9 }
    :printf("Enter in net receive section.\n")
    if (flag == 0) { : presynaptic spike  (after last post so depress)
	:printf("from pre to post. %g\n", flag)
	:printf("before g = %g\n",g)
	:printf("the w to add is %g",w)
	g = g + w
	:printf("after g = %g\n",g)
	if(learning) {
	    :printf("enter the learning section.\n")
	    if (w>=minWeight){
		w = w-(1+forDA)*LR*d*exp((tpost - t)/dtau)
		:printf("after w = %g\n",w)
		if(w<=minWeight){
		    w=minWeight
		}
		:w = w*LR*d*(1-(exp((tpost - t)/dtau)))
		:if(verbose) {
		 :   printf("dep: w=%g \t dw=%g \t dt=%g\n", w, -LR*d*exp((tpost - t)/dtau), tpost-t)
		:}
	    }
	}
	tpre = t
    }else if (flag == 2) { : postsynaptic spike
	:printf("now is here(post to pre) %g \n",flag)
	tmp=forSpike
	if ( forSpike == 0){
	    :skip to change forSpike
	}else{
	    forSpike=1
	}
	
	:if(forSpike!=tmp){
	 :   printf("forSpike is changed!!\n")
	:}
	
	tpost = t
	FOR_NETCONS(w1,tp){
            if(learning) {
	:	printf("enter the learning section\n")
		if(w1<=maxWeight){
	            w1 = w1 + (1+forDA)*LR*p*exp((tp-t)/ptau):w1 = w1+LR*p*exp((tp - t)/ptau)
	:	    printf("after w1 = %g\n",w1)
		}
		if(w1>maxWeight){:if (w1>maxWeight){
	            w1=maxWeight:w1 = maxWeight
		}
	:	if(verbose) {
	 :           printf("pot: w=%g \t dw=%g \t dt=%g\n", w1, (LR*p*exp((tp - t)/ptau)), t - tp)
	:	}
	    }
	}
	
    } else { : flag == 1 from INITIAL block
	:printf("else section")
	WATCH (v > -20) 2
    }
}
