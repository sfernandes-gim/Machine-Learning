import numpy as np

np.random.seed(42)

X = np.random.rand(5,4)
Y = np.array([[0.5],[0.6],[0.3],[0.8],[0.3]])

#Add the bias term to X implicitly X0
m = X.shape[0]
bias = np.ones((m, 1))

X= np.concatenate([bias,X],axis = 1)

learning_rate = 0.01
# Initialise Weights
weights = np.random.rand(m,1)
epochs = 100

for epoch in range(epochs):
    # Forward Prop
    ypred = np.dot(X,weights) 
    
    #Calculate Error MSE 
    loss = (1/(2*m))*np.sum((Y-ypred)**2)
    
    grad = (1/m)*np.dot(X.T,ypred-Y)
    
    weights -=learning_rate*grad
    
    if epoch % 20==0:
        print ("Epoch",epoch)
        print ("Loss",loss)
        

print("\nFinal Weights")
print(weights)


