import math
import numpy as np
# Financial Information and Analytics
# Assignment 1
# By Rajat Sudagade (UTD ID: 2021449378)

# Discounted Cash Flow and Bonds

# Part 1: Discounted Cash Flow

# Question 1: If you put up $31,000 today in exchange for a 6.25 percent, 14-year annuity, what will the annual cash flow?
def DCF1():
  r = 0.0625 # Rate per period = 6.25% 
  NPV = 31000 # Net present value = $31,000
  n = 14 # Number of periods = 14
  C = (r * NPV)/(1 - (1 + r)**(-n)) # Annual cash flow = (r * NPV)/(1 - (1 + r)**(-n)) = $3,386.9523610847937
  print("""Answer 1: 
  The annual cash flow will be ${:,.2f}\n""".format(C)) # print function for answer 1

# Question 2: Live Forever Life Insurance Co. is selling a perpetuity contract that pays $1,200 monthly.
# The contract currently sells for $61,000?
# a) What is the monthly return on this investment vehicle?
# b) What is the APR? (Do not round your intermediate calculations.)
# c) What is the effective annual rate? (Do not round your intermediate calculations.)
def DCF2():
  PV = 61000 # Present value of the contract = $61,000
  C = 1200 # Perpetuity contract pays $1,200 monthly
  r = C/PV # the monthly return on this investment vehicle = C/PV = 0.019672131147540985
  m = 12 # The number of months in a year
  APR = m * r # The annual percentage rate (APR) is calculated by multiplying the monthly return by 12 (number of months in the year) = 0.2360655737704918 
  EAR = ((1 + (APR / m)) ** (m)) - 1 # The effective annual rate (EAR) is 
  print("""Answer 2:
  a) The montly return on this investment vehicle is {:,.2f}%\n
  b) The Annual Percentage Rate (APR) is {:,.2f}%\n
  c) The Effective Annual Rate (EAR) is {:,.2f}%\n""".format(r*100, APR*100, EAR*100)) # Print function for Answer 2

# Question 3: Suppose an investment offers to triple your money in 72 months (but you don’t believe it,prove it).
# What rate of return per quarter are you being offered?
def DCF3():
  PV = 1 # Assume that the present value of the investment is $1
  FV = 3 # If the investment offers to triple our money, the future value will be #3
  months = 72 # total duration of the investment is 72 months
  n = (months / 12) * 4 # The number of periods in the investment periods
  i = ((FV/PV)**(1/n)) - 1
  print("""Answer 3:
  The rate of return per quarter that we are being offered here is {:,.2f}%\n""".format(i*100)) # Print function for Question 3 

# Question 4: You have just won the lottery and will receive $540,000 in one year. You will receive
# payments for 16 years, which will increase 5 percent per year. The appropriate discount rate
# is 10 percent.
# What is the present value of your winnings?
def DCF4():
  P = 540000 # First Payment = $540,000
  n = 16 # Number of periods = 16 years
  g = 0.05 # Growth rate = 5%
  r = 0.1 # Discount rate = 10%
  PV = ((P / (r - g)) * (1 - ((1 + g)/(1 + r))**(n)))
  print("""Answer 4: 
  The present value of the winnings is ${:,.2f}\n""".format(PV))

# Question 5: You're prepared to make monthly payments of $380, beginning at the end of this month, into an account that pays 8 percent interest compounded monthly.
# How many payments will you have made when your account balance reaches $25,694?
# (Do not round your intermediate calculations.)
def DCF5():
  FV = 25694 # Future Value = $25,694
  MP = 380 # Monthly Payments = $380
  k = 12 # number of months in a year
  r = 0.08 # interest
  t = (math.log(1 + ((FV/MP) * (r / k))))/(math.log(1 + (r / 12)))
  print("""Answer 5:
  Number of payments that we will have to make to reach $25,694 = {:,.2f}\n""".format(t))

# Question 6: You need a 30-year, fixed-rate mortgage to buy a new home for $230,000. 
# Your mortgage bank will lend you the money at a 7.6 percent APR for this 360-month loan. 
# However, you can afford monthly payments of only $800, so you offer to pay off any remaining loan balance at the end of the loan in the form of a single balloon payment.
# How large will this balloon payment have to be for you to keep your monthly payments at $800?
def DCF6():
  HP = 230000 # Price of a new home
  r = 0.076 # Interest rate = 7.6%
  DMP = 800 # Desired monthly payments = $800
  k = 12 # Number of months in a year
  m = 360 # Number of months in the total mortgage period = 30 years * 12 months = 360 months
  pva = (DMP * ((1 - ((1 / (1 + (r / k))) ** (m))) / (r / k))) # present value of the monthly payments
  ASO = HP - pva # Amount still owed = Price of a new home - present value of the monthly payments
  BP = ASO * ((1 + (r / k)) ** (m)) # Balloon payment at the end o the loan term
  print("""Answer 6: 
  Balloon payment in order to keep our monthly payments at $800 = ${:,.2f}\n""".format(BP))

# Question 7: You have just purchased a new warehouse. To finance the purchase, you've arranged for a 30-year mortgage loan for 80 percent of the $2,800,000 purchase price. The monthly payment on this loan will be $17,000.
# (a) What is the APR on this loan?
# (b) What is the EAR?
def DCF7():
  m = 30 # duration of mortgage loan = 30 years
  n = m * 12 # Because we are considering monthly payments, we need to multiply m by number of months in a year = 360
  r = 0.8 # interest rate = 80%
  TP = 2800000 # Total Price = $2,800,000
  MP = TP * r # Mortgage loan price = 80% of Total Price = $2,240,000
  P = 17000 # Monthly Payment = $17,000
  rate = np.rate(nper=n,pmt=P,pv=MP,fv=0,when='end')*12
  APR = rate
  EAR = ((1 + (APR/12))**(12))-1
  print("""Answer 7:
  a) The APR on this loan is: {0:,.2f}%
  b) The EAR is: {1:,.2f}%\n""".format(APR*100, EAR*100))
# Question 8: A 16-year annuity pays $1,700 per month, and payments are made at the end of each month. 
# The interest rate is 13 percent compounded monthly for the first Six years and 10 percent compounded monthly thereafter.
# What is the present value of the annuity?
# For the first 6 years
def DCF8():
  P = 1700 # Monthly payment = #1700
  i6 = 0.13 # Interest rate for first 6 years
  frequency = 12 # Because compounding is done montly
  yearOne = 6 # Term for first part
  i10 = 0.1 # Interest rate for the remaining 10 years
  yearTwo = 10 # Term for the second part
  PV = P*((1-(1+(i6/frequency))**(-yearOne*frequency))/(i6/frequency))+(P*((1-(1+(i10/frequency))**(-yearTwo*frequency))/(i10/frequency)))/(1+(i6/frequency))**(yearOne*frequency)
  print("""Answer 8:
  The present value of the annuity is ${:,.2f}\n""".format(PV))

# Question 9: You want to buy a new sports car from Muscle Motors for $43,000. 
# The contract is in the form of a 60-month annuity due at an 8.25 percent APR.
# What will your monthly payment be?
def DCF9():
  PVA = 43000 # Value of the car = $43,000
  i = 0.0825 # Interest = 8.25%
  term = 60 # Term = 60 months
  monthlyI = i/12 # Monthly interest = 0.6875%
  A = PVA/((1 - (1 + monthlyI)**(-term))/monthlyI)
  print("""Answer 9:
  The monthly payment will be: ${:,.2f}\n""".format(A))

# Question 10: You are looking at a one-year loan of $5,000. 
# The interest rate is quoted as 10 percent plus 3 points. 
# A point on a loan is simply 1 percent (one percentage point) of the loan amount. Quotes like this one is common with home mortgages. 
# The interest rate quotation in this example requires the borrower to pay 3 points to the lender up front and repay the loan later with 10 percent interest.
# What rate would you be paying, actually?
def DCF10():
  loan = 5000 # one-year loan of $5,000
  interest = 0.1
  points = 3 
  initP = loan*(points/100)
  effectiveLoan = loan - initP 
  valueOfLoan = (1 + interest)*loan
  effectiveInterest = (valueOfLoan/effectiveLoan) - 1
  print("""Answer 10:
  We would be paying the loan with an interest rate of: {:,.2f}%\n""".format(effectiveInterest*100))


# Part 2: Bonds

# Question 1: Staind, Inc., has 6 percent coupon bonds on the market that have 14 years left to maturity. 
# The bonds make annual payments. 
# If the YTM on these bonds is 10 percent, what is the current bond price? 
# Assume a par value of $1,000.
def BONDS1():
  r = 0.06 # Coupon Rate = 6%
  t = 14 # Years left to maturity = 14
  YTM = 0.1 # Yeild to maturity = 10%
  par = 1000
  ap = par*r # Annual payments = $1000 (Assumed) * 0.06 = 60
  pva = (1 - ((1 + YTM)**(-t)))/YTM # Present value of annuity factor = 7.366687457
  pvd = (1 + YTM)**(-t) # Present value of discounting = 0.263331254
  cp = ap * pva + par * pvd
  print("""Answer 1:
  The current bond price is: ${:,.2f}\n""".format(cp))

# Question 2: Ackerman Co. has 9 percent coupon bonds on the market with fourteen years left to maturity. 
# The bonds make annual payments. 
# If the bond currently sells for $850.46, what is its YTM? 
# Assume a par value of $1,000.
def BONDS2():
  r = 0.09 # Coupon rate = 9%
  par = 1000 # Par value = $1,000
  C = r * par # Annual coupon = $90
  frequency = 1
  t = 14 # Years left to maturity = 14
  nper = t * frequency
  pv = 850.46 # Selling price = $850.46
  YTM = (np.rate(nper = nper, pmt = C, pv = pv, fv = par))
  print("""Answer 2:
  The Yield to maturity is: {:,.2f}%\n""".format(YTM*100))

# Question 3: Kiss the Sky Enterprises has bonds on the market making annual payments, with 6 years to maturity, and selling for $970. 
# At this price, the bonds yield 9.9 percent. 
# What must the coupon rate be on the bonds?
def BONDS3():
  face = 1000 # Face value = $1000
  cp = 970 # Current Price = $970
  maturity = 6 # Time to maturity = 6 years
  yields = 0.099 # The bond yields at 9.9%
  PVIFA = (1 - ((1 + yields)**(-maturity)))/yields # Present Value Interest Factor of Annuity
  PVIF = ((1 + yields)**(-maturity)) # Present Value Interest Factor
  ac = (cp - (face * PVIF))/PVIFA # Annual Coupon = $92.131
  acr = ac/face # Annual Coupon Rate = 9.21%
  print("""Answer 3:
  The Annual Coupon Rate on the bonds is {:,.2f}%\n""".format(acr*100))

# Question 4: Grohl Co. issued 17-year bonds a year ago at a coupon rate of 8 percent. 
# The bonds make semiannual payments. 
# If the YTM on these bonds is 12 percent, what is the current bond price?
def BONDS4():
  years = 17-1 # Duration of bonds = 17 years - 1 (because the bonds were issued one year ago) = 16
  cr = 0.08 # Coupon rate = 8%
  ytm = 0.12 # Yield to Maturity = 12%
  tp = years * 2 # Since the bonds make semiannual payments, 16years * 2 = 32
  cpr = ytm/2 # Coupon rate = 12%/2 = 6%
  face = 1000
  ac = face * (cr/2)
  PVIFA = (1 - ((1 + (cpr))**(-tp)))/cpr
  PVIF = ((1 + cpr)**(-tp))
  P = ac *  PVIFA + face * PVIF
  print("""Answer 4:
  The Current Bond Price is ${:,.2f}\n""".format(P))

# Question 5: Ngata Corp. issued 19-year bonds 2 years ago at a coupon rate of 9.4 percent. 
# The bonds make semiannual payments. 
# If these bonds currently sell for 102 percent of par value, what is the YTM?
def BONDS5():
  fv = 1000 # Face value = $1,000
  cbpq = 1.02 # current bond price quote = 102%
  cr = 0.094 # Coupon rate = 9.4%
  ytm = 19-2 # Years to maturity = 19-2 (because bonds were issued 2 years ago) = 17
  scr = cr/2 # Semi-annual coupon rate = 4.7%
  scp = fv * scr # Semi-annual Coupon Price = $47
  ncp = ytm*2 # Number of compounding periods = 17*2 = 34
  cbp = fv * cbpq # Current bond price = $ 1020
  YTM = ((scp + ((fv-cbp)/ncp))/((fv + cbp)/2))*2
  print("""Answer 5: 
  The YTM here is: {:,.2f}%\n""".format(YTM*100))

# Question 6: Ashes Divide Corporation has bonds on the market with 17 years to maturity, a YTM of 11.0 percent, and a current price of $1,236.50. 
# The bonds make semiannual payments. 
# What must the coupon rate be on these bonds?
def BONDS6():
  years = 17 # Years to Maturity = 17 years
  YTM = 0.11 # YTM = 11%
  currentPrice = 1236.50 # Current price of the bond = 1,236.50
  fv = 1000 # Face value = $1000
  periods = years * 2 # No of periods will be 17 years * 2 because bonds make semiannual payments = 34
  rate = YTM/2 # This indicates the semi-annual YTM as = 0.055
  PVIFA = ((1 - ((1 + rate)**(-periods))))/rate
  PVIF = ((1 + rate)**(-periods))
  C = (currentPrice - (fv * PVIF))/PVIFA
  ac = C * 2 # Annual Coupon = $141.04
  cr = ac/fv # Coupon Rate = 14.10%
  print("""Answer 6:
  The Coupon Rate of these bonds is: {:,.2f}%\n""".format(cr*100))

# Question 7: Suppose the real rate is 5.5 percent and the inflation rate is 2 percent, what rate would you expect to see on a Treasury bill?
def BONDS7():
  rr = 0.055 # Real Rate = 5.5%
  ir = 0.02 # Inflation Rate = 2%
  rate = ((1 + ir)*(1 + rr))-1 # 1 + nr = (1 + ir)(1 + rr)
  print("""Answer 7:
  The Rate of a treasury bill would be: {:,.2f}%\n""".format(rate*100))

# Question 8: An investment offers a 13.0 percent total return over the coming year, 
# Bill Bernanke thinks the total real return on this investment will be only 6.5 percent. 
# What does Bill believe the inflation rate will be over the next year?
def BONDS8():
  nr = 0.13 # Nominal Rate = 13%
  rr = 0.065 # Real Rate = 6.5%
  ir = ((nr + 1)/(rr + 1)) - 1 # Inflation Rate
  print("""Answer 8:
  The Inflation Rate over the next year will be: {:,.2f}%\n""".format(ir*100))

# Question 9: Say you own an asset that had a total return last year of 9.5 percent. If the inflation rate last year was 5 percent, what was your real return?
def BONDS9():
  nr = 0.095 # Nominal Rate = 9.5%
  ir = 0.05 # Inflation Rate = 5%
  rr = ((1 + nr)/(1 + ir)) - 1
  print("""Answer 9:
  The Real Return was {:,.2f}%\n""".format(rr*100))

# Question 10: Both Bond Sam and Bond Dave have 6 percent coupons, make semiannual payments, and are priced at par value. 
# Bond Sam has 3 years to maturity, whereas Bond Dave has 18 years to maturity. (Do not round your intermediate calculations.)
# a) If interest rates suddenly rise by 4 percent, what is the percentage change in the price of Bond Sam? 
# b) If interest rates suddenly rise by 4 percent, what is the percentage change in the price of Bond Dave?
# c) If interest rates suddenly fall by 4 percent, what is the percentage change in the price of Bond Sam be then?
# d) If interest rates suddenly fall by 4 percent, what is the percentage change in the price of Bond Dave be then?
def BONDS10():
  def func1(yields, maturity):
    return (1 - ((1 + yields)**(-maturity)))/yields
  def func2(yields, maturity):
    return ((1 + yields)**(-maturity))
  # a and b
  sam = 1000 # Assume price of sam's bond to be $1000
  dave = 1000 # Assume price of dave's bond to be $1000
  oldYTM = 0.06/2
  sc = sam*oldYTM
  samYears = 3
  daveYears = 18
  samPeriods = samYears * 2
  davePeriods = daveYears * 2
  newYTM = 0.10/2
  samPVIFA = func1(yields=newYTM, maturity=samPeriods)
  samPVIF = func2(yields=newYTM, maturity=samPeriods)
  davePVIFA = func1(yields=newYTM, maturity=davePeriods)
  davePVIF = func2(yields=newYTM, maturity=davePeriods)
  newSamPrice =  sc * samPVIFA + sam * samPVIF
  newDavePrice = sc * davePVIFA + dave * davePVIF
  sampercentChange = (newSamPrice - sam)/sam 
  davepercentChange = (newDavePrice - dave)/dave
  # c and d
  newerYTM = 0.02/2
  newSamPVIFA = func1(yields=newerYTM, maturity=samPeriods)
  newSamPVIF = func2(yields=newerYTM, maturity=samPeriods)
  newDavePVIFA = func1(yields=newerYTM, maturity=davePeriods)
  newDavePVIF = func2(yields=newerYTM, maturity=davePeriods)
  newerSamPrice = sc * newSamPVIFA + sam * newSamPVIF
  newerDavePrice = sc * newDavePVIFA + dave * newDavePVIF
  newSamPercentChange = (newerSamPrice - sam)/sam
  newDavePercentChange = (newerDavePrice - dave)/dave
  print("""Answer 10:
  a) If interest rates suddenly rise by 4 percent, the percentage change in the price of Bond Sam will be {0:,.2f}%
  b) If interest rates suddenly rise by 4 percent, the percentage change in the price of Bond Dave will be {1:,.2f}%
  c) If interest rates suddenly fall by 4 percent, the percentage change in the price of Bond Sam will be {2:,.2f}%
  d) If interest rates suddenly fall by 4 percent, the percentage change in the price of Bond Dave will be {3:,.2f}%\n""".format(sampercentChange*100, davepercentChange*100, newSamPercentChange*100, newDavePercentChange*100))

print("""Financial Information and Analytics\n
Assignment 2\n
Discounted Cash Flow and Bonds\n
By Rajat Sudagade (UTD ID 2021449378)\n""")
def menu():
  a = int(input("Press 1 for Discounted Cash Flow\nPress 2 for Bonds\nPress 3 for All\nPress any other number to exit\n"""))
  if (a == 1):
    print("\n")
    print("Displaying Part 1: Discounted Cash Flows\n")
    DCF1()
    DCF2()
    DCF3()
    DCF4()
    DCF5()
    DCF6()
    DCF7()
    DCF8()
    DCF9()
    DCF10()
    menu()
  elif (a == 2):
    print("\n")
    print("Displaying Part 2: Bonds\n")
    BONDS1()
    BONDS2()
    BONDS3()
    BONDS4()
    BONDS5()
    BONDS6()
    BONDS7()
    BONDS8()
    BONDS9()
    BONDS10()
    menu()
  elif (a == 3):
    print("\n")
    print("Displaying Part 1: Discounted Cash Flows\n")
    DCF1()
    DCF2()
    DCF3()
    DCF4()
    DCF5()
    DCF6()
    DCF7()
    DCF8()
    DCF9()
    DCF10()
    print("\n")
    print("Displaying Part 2: Bonds\n")
    BONDS1()
    BONDS2()
    BONDS3()
    BONDS4()
    BONDS5()
    BONDS6()
    BONDS7()
    BONDS8()
    BONDS9()
    BONDS10()
    menu()
  else:
    pass

menu()