def studentReg(ages_train, net_worths_train):
    ### import the sklearn regression module, create, and train your regression
    from sklearn import linear_model
    reg = linear_model.LinearRegression()
    reg.fit(ages_train, net_worths_train)
    return reg 
