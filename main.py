from numpy import cos, sin, pi, linspace, ndarray
import matplotlib.pyplot as plt


def get_function(prompt: str):
    start_index = 0

    if prompt[0].isdigit():
        start_index += 1

    T = 2 / int(prompt[prompt.index("(") + 1 :].split("*")[0])
    interval = (-T, 3 * T)
    t = linspace(interval[0], interval[1], 1000)

    return t, eval(prompt)


prompt = "cos(1000*pi*t-pi/6)"
prompt2 = "sin(1000*pi*t+pi/6)"
t, v = get_function(prompt)
t, v2 = get_function(prompt2)
v3 = v + v2
plt.plot(t, v, label=prompt)
plt.plot(t, v2, label=prompt2)
plt.plot(t, v3, label="v+v2")
plt.grid(True)
plt.legend()
plt.title("AC Voltage Graph")
plt.xlabel("Time (s)")
plt.ylabel("Voltage (V)")
plt.show()
