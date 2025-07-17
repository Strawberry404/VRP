import streamlit as st
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

# Set Streamlit title
st.title("🚛 AI-Powered Vehicle Routing & Demand Prediction")

# Sidebar - User Inputs for Parameters
st.sidebar.header("📌 Adjust Simulation Parameters")

num_clients = st.sidebar.slider("Number of Clients", 10, 100, 80)
num_vehicles = st.sidebar.slider("Number of Vehicles", 1, 20, 10)
max_capacity = st.sidebar.slider("Vehicle Capacity", 500, 5000, 1000)
max_time = st.sidebar.slider("Max Delivery Time (mins)", 10, 60, 30)
prediction_days = st.sidebar.slider("Prediction Period (days)", 7, 60, 30)

st.sidebar.write("**🔄 Adjust values & see real-time optimization!**")

# Simulated ANN Demand Predictions
st.subheader("📈 Demand Forecast (Predicted by ANN)")
predicted_demand = np.random.randint(100, 500, size=(num_clients,))
st.bar_chart(predicted_demand)

# Generate Random Client Positions
np.random.seed(42)
client_positions = {i: (np.random.rand() * 100, np.random.rand() * 100) for i in range(num_clients)}

# Example Optimized Route from ACO
optimized_route = list(np.random.permutation(num_clients))  # Random permutation for now

# Create Graph for VRP
G = nx.DiGraph()
for client, pos in client_positions.items():
    G.add_node(client, pos=pos)

edges = [(optimized_route[i], optimized_route[i+1]) for i in range(len(optimized_route)-1)]
G.add_edges_from(edges)

# Plot the Optimized Route
st.subheader("🚗 Optimized Vehicle Routing Plan")
fig, ax = plt.subplots(figsize=(10, 6))
pos = nx.get_node_attributes(G, 'pos')
nx.draw(G, pos, with_labels=True, node_color="lightblue", edge_color="red", width=2, node_size=500, font_size=8)
nx.draw_networkx_nodes(G, pos, nodelist=[0], node_color="green", node_size=800, label="Depot")
plt.title("Optimized Vehicle Routing Plan (ACO + ANN Demand)")
plt.legend()
st.pyplot(fig)

# Display Route Order
st.subheader("📍 Best Route Found")
st.write("🚦 Optimized Route Order:", optimized_route)
