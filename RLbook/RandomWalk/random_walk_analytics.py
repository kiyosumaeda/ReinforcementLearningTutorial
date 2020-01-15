import matplotlib.pyplot as plt

def read_rms(l, filename):
	with open(filename, "r") as f:
		for row in f:
			l.append(float(row)/100)

rms_01 = []
rms_015 = []
rms_005 = []
rms_mc_01 = []
rms_mc_02 = []
rms_mc_03 = []
rms_mc_04 = []

read_rms(rms_01, "rms_0_1.txt")
read_rms(rms_015, "rms_0_15.txt")
read_rms(rms_005, "rms_0_05.txt")
read_rms(rms_mc_01, "rms_mc_0_01.txt")
read_rms(rms_mc_02, "rms_mc_0_02.txt")
read_rms(rms_mc_03, "rms_mc_0_03.txt")
read_rms(rms_mc_04, "rms_mc_0_04.txt")

plt.figure(figsize=(12, 6))
plt.title("Empiriacal RMS error, averaged over states")
plt.xlabel("Walks/Episodes")
plt.plot(rms_01, color="blue", label="α=.1")
plt.plot(rms_015, color="blue", label="α=.15")
plt.plot(rms_005, color="blue", label="α=.05")
plt.plot(rms_mc_01, color="red", label="α=.01")
plt.plot(rms_mc_02, color="red", label="α=.02")
plt.plot(rms_mc_03, color="red", label="α=.03")
plt.plot(rms_mc_04, color="red", label="α=.04")
plt.show()
