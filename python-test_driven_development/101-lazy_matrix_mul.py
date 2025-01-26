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

    if not (isinstance(m_a, list)) or not (isinstance(m_b, list)):
        raise TypeError("Scalar operands are not allowed, use '*' instead")
    # result = np.multiply(m_a, m_b)
    result = np.matmul(m_a, m_b)
    return (result)
