import csv
import random
import statistics
import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go

df = pd.read_csv("medium_data.csv")
data = df["reading_time"].tolist()

mean = statistics.mean(data)
std_deviation = statistics.stdev(data)

print("Population mean --> ", mean)
print("Population Std Deviation --> ", std_deviation)

def random_set_of_means(counter):
    dataset = []
    for i in range(0, counter):
        random_index = random.randint(0, len(data) - 1)
        value = data[random_index]

        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean
    
mean_list = []

for i in range(0, 100):
    set_of_means = random_set_of_means(30)
    mean_list.append(set_of_means)

sampling_mean = statistics.mean(mean_list)
sampling_std_deviation = statistics.stdev(mean_list)

first_std_deviation_start, first_std_deviation_end = sampling_mean-sampling_std_deviation, sampling_mean+sampling_std_deviation
second_std_deviation_start, second_std_deviation_end = sampling_mean-(2*sampling_std_deviation), sampling_mean+(2*sampling_std_deviation)
third_std_deviation_start, third_std_deviation_end = sampling_mean-(3*sampling_std_deviation), sampling_mean+(3*sampling_std_deviation)

print("First Std Deviation --> ", first_std_deviation_start,", ", first_std_deviation_end)
print("Second Std Deviation --> ", second_std_deviation_start,", ", second_std_deviation_end)
print("Third Std Deviation --> ", third_std_deviation_start,", ", third_std_deviation_end)

fig = ff.create_distplot([mean_list], ["READING TIME"], show_hist=False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 1], mode="lines", name="MEAN"))
fig.add_trace(go.Scatter(x=[sampling_mean, sampling_mean], y=[0, 1], mode="lines", name="SAMPLING MEAN"))
fig.add_trace(go.Scatter(x=[first_std_deviation_start, first_std_deviation_start], y=[0, 1], mode="lines", name="1ST STD DEVIATION START"))
fig.add_trace(go.Scatter(x=[first_std_deviation_end, first_std_deviation_end], y=[0, 1], mode="lines", name="1ST STD DEVIATION END"))
fig.add_trace(go.Scatter(x=[second_std_deviation_start, second_std_deviation_start], y=[0, 1], mode="lines", name="2ND STD DEVIATION START"))
fig.add_trace(go.Scatter(x=[second_std_deviation_end, second_std_deviation_end], y=[0, 1], mode="lines", name="2ND STD DEVIATION END"))
fig.add_trace(go.Scatter(x=[third_std_deviation_start, third_std_deviation_start], y=[0, 1], mode="lines", name="3RD STD DEVIATION START"))
fig.add_trace(go.Scatter(x=[third_std_deviation_end, third_std_deviation_end], y=[0, 1], mode="lines", name="3RD STD DEVIATION END"))
fig.show()

z_score = (sampling_mean - mean)/sampling_std_deviation
print(f"Z Score --> {z_score}")