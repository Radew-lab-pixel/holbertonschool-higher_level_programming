#!/usr/bin/python3
""" 101-lazy_matrix_mul.py """
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    function to multiply two matrix using numpy

    Args:
        m_a : matrix
        m_b : matrix
    Returns:
        m_a * m_b
    """

    result = np.multiply(m_a, m_b)
    return (result)
