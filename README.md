# Federated_Learning
Hierarchical Federated Learning. 
The Feature extraction global model located in Edge Node(BackBone Network).
The Classifier model(FCN) located in Client Node.

The code written here confirms that the whole model with frozen feature extraction layer and the small model with fcn layers shows the same performance.
Also to send the feature extracted data from the edge node to client node, I implemented the GRPC based data transmission strategy.
