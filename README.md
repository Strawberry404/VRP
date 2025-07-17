# VRP and ANN Coupling with ACO

## Overview

This project addresses the complex Vehicle Routing Problem (VRP) using a fleet of N80 K10 vehicles and demand prediction through Artificial Neural Networks (ANN). The optimization of routes is achieved using the Ant Colony Optimization (ACO) algorithm with an interactive user interface to tweak parameters.

## Features

- **Demand Prediction**: Uses Artificial Neural Networks (ANN) to predict customer demand based on historical data
- **Route Optimization**: Implements Ant Colony Optimization (ACO) algorithm for solving the Vehicle Routing Problem
- **Interactive Parameters**: Provides an interactive interface for adjusting ACO algorithm parameters
- **Data Visualization**: Includes comprehensive data analysis and visualization tools
- **Fleet Management**: Handles a fleet of N80 K10 vehicles for optimal route planning

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/username/VRP-pushed.git
   cd VRP-pushed
   ```

2. **Install the required packages:**

   Install the necessary Python packages using pip:

   ```bash
   pip install pandas numpy tensorflow sklearn matplotlib sweetviz missingno
   ```

## Usage

1. **Load and preprocess the data:**
   - Import product data from `data.csv` using pandas
   - The dataset contains Product_Code, Product_Category, Date, and Order_Demand columns

2. **Train the ANN model:**
   - Use TensorFlow and scikit-learn for data normalization and model training
   - Implement neural network layers with dropout for demand prediction

3. **Optimize routes using ACO:**
   - Adjust ACO parameters via the provided interface
   - Compute optimal routes for the vehicle fleet

4. **Run the Jupyter Notebook:**
   Launch Jupyter notebook and open the main implementation file:
   ```bash
   jupyter notebook "Couplage entre la prédiction de la demande ANN et le VRP avec ACO.ipynb"
   ```

## Dataset

The project uses historical product data with the following structure:
- **Product_Code**: Unique identifier for products
- **Product_Category**: Category classification of products
- **Date**: Transaction date
- **Order_Demand**: Demand quantity for each product

## Files

- `Couplage entre la prédiction de la demande ANN et le VRP avec ACO.ipynb`: Main notebook with all implementations
- `data.csv`: Dataset used for training the ANN model
- `.ipynb_checkpoints/`: Jupyter notebook checkpoints folder

## Dependencies

- Python 3.x
- Jupyter Notebook
- **Data Processing**: Pandas, Numpy
- **Machine Learning**: TensorFlow, Keras, Scikit-learn
- **Visualization**: Matplotlib, Sweetviz, Missingno
- **Preprocessing**: MinMaxScaler, LabelEncoder

## Technical Implementation

### 1. Data Preprocessing
- Data cleaning and missing value handling
- Feature scaling using MinMaxScaler
- Label encoding for categorical variables

### 2. ANN Model
- Sequential neural network architecture
- Dense layers with dropout for regularization
- Input layer for feature processing
- Output layer for demand prediction

### 3. ACO Algorithm
- Ant colony optimization for route planning
- Interactive parameter tuning interface
- Vehicle capacity constraints handling
- Distance matrix optimization

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Author

- **Project**: VRP and ANN Coupling with ACO
- **Implementation**: Demand prediction and route optimization system
- **Contact**: For questions and support

## Acknowledgments

- TensorFlow and Keras for neural network implementation
- Scikit-learn for machine learning utilities
- Pandas and NumPy for data processing
- Matplotlib and Sweetviz for data visualization

---

*This project demonstrates the integration of machine learning techniques with optimization algorithms for solving real-world logistics problems.*

