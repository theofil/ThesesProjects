
# Introduction
At the <a href="https://home.cern/science/accelerators/large-hadron-collider"> LHC</a>, 
protons traveling almost with the speed of light are smashed together with other protons traveling with the same speed but in the opposite direction.

The resulting interactions among the LHC colliding protons (pp -> X) is a hot topic for <a href="https://en.wikipedia.org/wiki/Particle_physics">high energy physics</a> 
with over a <a href="http://cms-results.web.cern.ch/cms-results/public-results/publications-vs-time/">thousand publications</a>, 
up to now by the <a href="http://cms.cern">CMS</a> experiment and a very similar scientific yield by the <a href="http://atlas.cern">ATLAS</a> experiment. 
There are four (known) fundamental forces, which are modeled by the theories of QCD, weak, QED and gravitational interactions. 
The first three are routinely studied with particle detectors at the LHC and are enjoying a common theoritical framework known as the <a href="https://en.wikipedia.org/wiki/Standard_Model">standard model</a>.

Provided that sufficient amount of energy is gathered in the center-of-momentum (<span>&#8730; s</span>) 
new particles and new interactions might take place. If kinematically allowed, the new particles will be produced
with probability (~cross section) dictated by the laws of relativistic quantum mechanics. 
Think of each pp collision as a dice, but instead of just 6 discrete faces (=1, 2, 3, 4, 5, 6) we have a continuous set of possible outcomes (probability density function), 
some of them are not even known or are predicted to exist but are very rare (e.g., the <a href="https://en.wikipedia.org/wiki/Higgs_boson">Higgs boson</a>).
By "rolling" our pp "dice" many times (accumulating luminosity) and increasing the <span>&#8730; s</span>, we are able to probe previously uncharted regions and increase our reach to new phenomena.

The basic question we try to answer: is the <a href="https://en.wikipedia.org/wiki/Standard_Model">standard model</a> 
breaking up when the (<span>&#8730; s</span>) gets large ? Are there the unexpected phenomena showing up indicating
<a href="https://en.wikipedia.org/wiki/Physics_beyond_the_Standard_Model">beyond the standard model</a> physics?

# Data Sample
The <a href="https://home.cern/science/experiments/cms">CMS</a> experiment has made available a very small subset of data recorded at <span>&#8730; s</span> = 7 TeV. 
The data sample consists of 100k events containing two <a href="https://en.wikipedia.org/wiki/Muon">muons</a>
```
pp -> μμ + X
```
in the final state.
You could see the the two muons while traversing the CMS detector as two red tracks, 

<img src = "http://theofil.web.cern.ch/theofil/images/eventDisplay.png">

originating from the pp interaction point, which is busy with many other yellow tracks from other charged particles (mostly hadrons, e.g., pions and kaons).
An interactive event display of the data sample is available <a href="http://opendata.cern.ch/record/303">here</a>.

From the curvature of the tracks inside the strong magnetic field of the CMS magnet (3.8 T), the momentum of the muons as well as their charge can be measured.
A sample of 100k dimuon events recorded by CMS has been publicly disseminated for educational and outreach reasons (DOI:10.7483/OPENDATA.CMS.4M97.3SQ9).
The original data files have been further reduced and simplified for the purpose of this introductory exercise. 
The information of four-momenta and the charge of the two muons is stored in a <a href="http://theofil.web.cern.ch/theofil/files/cms_dimuons.txt">csv file</a> (comma separated values).
Each line holds the charge (Q) and the four-momentum components (E, px, py, pz) of the two muons,
```
Q1,E1,px1,py1,pz1,Q2,E2,px2,py2,pz2
```
as measured (in units of GeV) by the CMS detector during the pp collisions.
For example, the first three lines of the csv file  read as following:
```
Q1,E1,px1,py1,pz1,Q2,E2,px2,py2,pz2
-1,7.3339,2.06042,5.8858,-3.85836,1,5.20755,-1.55016,-1.81976,4.62525
-1,18.4672,8.03395,-3.94072,-16.1541,1,10.7295,6.29476,-2.52441,-8.31349
...
```
with the 0th line being the header (column names) and the 2nd event showing up in the 2nd line, containing one muon of energy ~18.5 GeV and negative charge and another one of positive charge
with energy of ~10.7 GeV. 
More simple can't be made, no ?

# The Exercise
Download the data from the <a href="http://theofil.web.cern.ch/theofil/files/cms_dimuons.txt">csv file</a> and analyze them with any programming language you wish.
Some quick ideas to play with:
* Study the invariant mass distribution (histogram) of each muon, play with the binning and the scale and comment on your findings.
* Study the frequency of ++, -- and +- muon pairs.
* Investigate the possibility that the two muons originate from the decay of a heavier particle; estimate its mass and charge.
* Study your own ideas share with me your curiosity.


Going back to our analogy of a pp collision with a dice roll, we can compare data from dice rolls with simulated dice rolls having p = 1/6 for each face and infer whether the dice is fair or biased. The natural question arising is, how can we simulate the possible outcomes of pp collisions and confront them with data ? 
The answer is that we can only simulate what we know it is there (i.e., <a href="https://en.wikipedia.org/wiki/Standard_Model">standard model</a>) 
and hypothesized <a href="https://en.wikipedia.org/wiki/Physics_beyond_the_Standard_Model">beyond the standard model signals</a> we search for by using Monte Carlo generators such <a href="https://pythia.org">Pythia</a> and <a href="http://herwig.hepforge.org">Herwig</a>.
Confronting LHC data with theory predictions is called "LHC physics analysis" and can have as a result an academic thesis or even a nobel prize if we get lucky  ;-)

A real life example of data vs MC simulation is on Figure 3 from <a href="https://cms.cern/news/lhc-vector-boson-collider">this</a> physics analysis.
<br>
Interested to join the LHC physics program ? 









