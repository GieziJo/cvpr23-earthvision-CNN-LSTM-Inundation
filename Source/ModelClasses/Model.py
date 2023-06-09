from fastai.vision.all import *

class CNNLSTM(nn.Module):
    def __init__(self, nbFeatures=10, initSize=32, nbLayers=1, nbTimeSteps=10, input_size=32*32, hidden_size=32*32):
        super().__init__()
        
        self.nbFeatures = nbFeatures
        self.input_size = input_size
        self.nbTimeSteps = nbTimeSteps
        
        # define helper functions for convolutions, either single convolution, or combined with res block
        def conv2_single(ni,nf): return nn.Conv2d(ni, nf, kernel_size=3, padding=1, padding_mode='reflect', stride=1)
        def conv2(ni,nf): return nn.Conv2d(ni, nf, groups=nbTimeSteps, kernel_size=3, padding=1, padding_mode='reflect', stride=1)
        def conv2_and_res(ni, nf): return nn.Sequential(conv2(ni,nf), ResBlock(2, ni, nf, groups=nbTimeSteps, stride=1))
        
        # Create CNN A
        # note that groups are defined by number of time steps, i.e. each time step is applied the same CNN separatly
        self.cnn = nn.Sequential(
            conv2(nbFeatures*nbTimeSteps,nbTimeSteps*initSize)
        )
        
        for k in range(nbLayers):
            self.cnn = self.cnn.append(conv2_and_res(nbTimeSteps*initSize * 4**k, nbTimeSteps*(initSize * 2) * 4**k))
        self.cnn = self.cnn.append(conv2(nbTimeSteps*(initSize * 2) * 4**(nbLayers-1)* 2,nbTimeSteps*1))
        
        # Create LSTM
        self.LSTM = nn.LSTM(input_size=input_size, hidden_size=hidden_size, num_layers=1, batch_first=True, bidirectional=False)
        
        # Create transpose convolution
        self.convTrans = nn.ConvTranspose2d(1024,1,kernel_size=32)
        
        # Set the output to be a single convolution and a sigmoid
        self.outLayer = nn.Sequential(conv2_single(2,1), SigmoidRange(0,1))

    def forward(self, x):
        # get size of problem
        batchSize = x.shape[0]
        imgSize = x.shape[2:4]
        
        # pass all time steps through the CNN
        x = self.cnn(x)
        # extract time step 0
        x_now = x[:,0,::].view((batchSize,1,imgSize[0],imgSize[1]))
        # pass time step -1 to -9 through lstm
        x, (_,_) = self.LSTM(x[:,1:,::].view((batchSize,self.nbTimeSteps-1,-1)))
        # extract result and pass through transpose convolution
        x = x[:,-1,:].view((batchSize,-1,1,1))
        x = self.convTrans(x)
        # concatenate lstm output and time step t
        x = torch.cat((x_now,x),1)
        # pass output through output layer
        x = self.outLayer(x)
        return x