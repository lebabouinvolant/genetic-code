import neuralnetwork
import struct
import numpy as np
import matrix
import tkinter as tk



def load_images(path): #This is AI generated
    with open(path, "rb") as f:
        magic, n_images, rows, cols = struct.unpack(">IIII", f.read(16))

        data = np.frombuffer(
            f.read(),
            dtype=np.uint8
        )

        return data.reshape(n_images, rows * cols)


def load_labels(path): #This too (sorry but the mnist library doesn't work anymore)
    with open(path, "rb") as f:
        magic, n_labels = struct.unpack(">II", f.read(8))

        return np.frombuffer(
            f.read(),
            dtype=np.uint8
        )


xtrain = load_images("MNIST/train-images.idx3-ubyte").astype(np.float32) / 255.0
ytrain = load_labels("MNIST/train-labels.idx1-ubyte")
xcheck = load_images("MNIST/t10k-images.idx3-ubyte").astype(np.float32) / 255.0
ycheck = load_labels("MNIST/t10k-labels.idx1-ubyte")

ytrainTreated = []
for el in ytrain:
    ytrainTreated.append(matrix.Matrix([[0 if i != el else 1] for i in range(10)]))
model = neuralnetwork.NeuralNetwork(784, 128, 10, 0.01, 2)
epoch = 2
for i in range(epoch):
    perm = np.random.permutation(len(xtrain))
    xtrain_shuffled = xtrain[perm]
    ytrainTreated_shuffled = [ytrainTreated[j] for j in perm]
    model.allTrain(xtrain_shuffled, ytrainTreated_shuffled)


winrate = model.allTest(xcheck, ycheck)
print(f"Le modèle a un taux de succès de {winrate*100}%")
