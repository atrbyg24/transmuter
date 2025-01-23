import numpy as np
trials = 100000

"""
original is the current upgrade chances before version 5.5.
"""
def original(trials):
  CV_upgrades = np.zeros(6)
  for i in range(trials):
    upgrade_count = 0
    three_liner = np.random.randint(3)
    if three_liner < 2:
      upgrades = np.random.randint(4,size=4)
      for upgrade in upgrades:
        if upgrade < 2:
          upgrade_count += 1
      CV_upgrades[upgrade_count] += 1
    else:
      upgrades = np.random.randint(4,size=5)
      for upgrade in upgrades:
        if upgrade < 2:
          upgrade_count += 1
      CV_upgrades[upgrade_count] += 1
  CV_dist = CV_upgrades/trials
  EV = np.sum(np.array([i+2 for i in range(6)])*CV_dist)
  average_CV = 6.6 * (EV)
  min_CV = 5.44 * (EV)
  print(f'Using original the distribution is {CV_dist}')
  print(f'The expected number of rolls (excluding starting substats) is {EV-2}')
  print(f'The average CV with average rolls is {average_CV}')
  print(f'The average CV with min rolls is {min_CV}')
  print('\n')
  return

"""
firstTwo is one possible way to implement the chance where it is assumed that
the first two upgrade chances are guaranteed to be Crit.
"""
def firstTwo(trials):
    CV_upgrades = np.zeros(6)
    for i in range(trials):
      upgrade_count = 0
      three_liner = np.random.randint(3)
      if three_liner < 2:
        upgrades = np.random.randint(4,size=2)
        for upgrade in upgrades:
          if upgrade < 2:
            upgrade_count += 1
        CV_upgrades[upgrade_count+2] += 1
      else:
        upgrades = np.random.randint(4,size=3)
        for upgrade in upgrades:
          if upgrade < 2:
            upgrade_count += 1
        CV_upgrades[upgrade_count+2] += 1
    CV_dist = CV_upgrades/trials
    EV = np.sum(np.array([i+2 for i in range(6)])*CV_dist)
    average_CV = 6.6 * (EV)
    min_CV = 5.44 * (EV)
    print(f'Using firstTwo the distribution is {CV_dist}')
    print(f'The expected number of rolls (excluding starting substats) is {EV-2}')
    print(f'The average CV with average rolls is {average_CV}')
    print(f'The average CV with min rolls is {min_CV}')
    print('\n')
    return

"""
lastTwo is another way to implement the chance where it is assumed that
if the artifact piece has not been upgraded in Crit at least two times, then
one or both of the last two upgrade chances will be guaranteed to be Crit so
that the artifact piece has 2 upgrades in Crit. Essentially this consolidates
the chances of getting 0,1 or 2 upgrades into getting 2 upgrades.
"""
def lastTwo(trials):
    CV_upgrades = np.zeros(6)
    for i in range(trials):
      upgrade_count = 0
      three_liner = np.random.randint(3)
      if three_liner < 2:
        upgrades = np.random.randint(4,size=4)
        for upgrade in upgrades:
          if upgrade < 2:
            upgrade_count += 1
        CV_upgrades[upgrade_count] += 1
      else:
        upgrades = np.random.randint(4,size=5)
        for upgrade in upgrades:
          if upgrade < 2:
            upgrade_count += 1
        CV_upgrades[upgrade_count] += 1
    CV_upgrades[2] += CV_upgrades[0] + CV_upgrades[1]
    CV_upgrades[0] = 0
    CV_upgrades[1] = 0
    CV_dist = CV_upgrades/trials
    EV = np.sum(np.array([i+2 for i in range(6)])*CV_dist)
    average_CV = 6.6 * (EV)
    min_CV = 5.44 * (EV)
    print(f'Using lastTwo the distribution is {CV_dist}')
    print(f'The expected number of rolls (excluding starting substats) is {EV-2}')
    print(f'The average CV with average rolls is {average_CV}')
    print(f'The average CV with min rolls is {min_CV}')
    print('\n')
    return
