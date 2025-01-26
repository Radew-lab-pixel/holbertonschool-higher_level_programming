#!/usr/bin/python3
""" 100-matrix_mul.py """

def matrix_mul(m_a, m_b):
    """
    function to multiply two matrixs

    Args:
        m_a : first matrix
        m_b : second matrix

    Returns:
        m_a * m_b 
    """
    if not m_a or (m_a == []):
        raise ValueError("m_a can't be empty")
    if not m_b:
        raise ValueError("m_b can't be empty")
    
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TabError("m_b must be a list")
    # if not (isinstance(element, list) for element in lists for lists in m_a):
    
    # if not isinstance(m_a, (int, float)):
    if not all(isinstance(ele, list) for ele in m_a):
        raise TypeError("m_a must be a list of lists")
    # if not isinstance(m_b, (int, float)):
    if not all(isinstance(ele, list) for ele in m_b):
        raise TypeError("m_b must be a list of lists")
    
    num_rowsA = len(m_a)
    num_colsA = len(m_a[0])
    prev_cols = num_colsA
    for i in range(0, num_rowsA, 1):
        if (len(m_a[i]) != prev_cols):  # colummns diff
            raise TypeError("each row of m_a must be of the same size")
        prev_cols = len(m_a[i])

    num_rowsB = len(m_b)
    num_colsB = len(m_b[0])
    prev_cols = num_colsB
    for i in range(0, num_rowsB, 1):
        if (len(m_b[i]) != prev_cols):  # colummns diff
            raise TypeError("each row of m_b must be of the same size")
        prev_cols = len(m_b[i])

    result = [[sum(a * b for a, b in zip(A_row, B_col)) 
                        for B_col in zip(*m_b)]
                                for A_row in m_a]

    return (result)
