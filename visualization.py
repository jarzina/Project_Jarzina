"""
Utility functions for visualization in the Tox21 project.
These functions will be used across different notebooks to maintain consistent plotting styles.
"""

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
from typing import List, Union, Optional

def set_plotting_style():
    """
    Set consistent plotting style for the project.
    """
    plt.style.use('default')  # Use default style instead of seaborn
    sns.set_theme()  # Apply seaborn theme on top
    plt.rcParams['figure.figsize'] = [12, 8]
    plt.rcParams['font.size'] = 12
    
def plot_distribution(data: Union[np.ndarray, pd.Series],
                     title: str,
                     xlabel: str,
                     ylabel: str = 'Count',
                     save_path: Optional[str] = None):
    """
    Plot distribution of data with proper formatting for presentations.
    
    Parameters:
    -----------
    data : array-like
        Data to plot
    title : str
        Plot title
    xlabel : str
        X-axis label
    ylabel : str
        Y-axis label
    save_path : str, optional
        Path to save the figure
    """
    plt.figure(figsize=(12, 8))
    sns.histplot(data, kde=True)
    plt.title(title, fontsize=14, pad=20)
    plt.xlabel(xlabel, fontsize=12)
    plt.ylabel(ylabel, fontsize=12)
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
    plt.show()

def plot_correlation_matrix(corr_matrix: pd.DataFrame,
                          title: str = 'Correlation Matrix',
                          save_path: Optional[str] = None):
    """
    Plot correlation matrix with proper formatting.
    
    Parameters:
    -----------
    corr_matrix : pd.DataFrame
        Correlation matrix to plot
    title : str
        Plot title
    save_path : str, optional
        Path to save the figure
    """
    plt.figure(figsize=(12, 10))
    sns.heatmap(corr_matrix, 
                annot=True, 
                cmap='coolwarm', 
                center=0,
                fmt='.2f')
    plt.title(title, fontsize=14, pad=20)
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
    plt.show()

def plot_model_performance(metrics: dict,
                         title: str,
                         save_path: Optional[str] = None):
    """
    Plot model performance metrics.
    
    Parameters:
    -----------
    metrics : dict
        Dictionary containing metric names and values
    title : str
        Plot title
    save_path : str, optional
        Path to save the figure
    """
    plt.figure(figsize=(10, 6))
    bars = plt.bar(range(len(metrics)), list(metrics.values()))
    plt.xticks(range(len(metrics)), list(metrics.keys()), rotation=45)
    plt.title(title, fontsize=14, pad=20)
    plt.ylabel('Score', fontsize=12)
    
    # Add value labels on top of bars
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2., height,
                f'{height:.3f}',
                ha='center', va='bottom')
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
    plt.show() 