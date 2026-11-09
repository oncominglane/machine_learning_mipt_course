import numpy as np


def build_precision_recall_curve(
    true_labels: np.ndarray, predicted_probas: np.ndarray
) -> np.ndarray:
    """
    Данная функция строит PR-кривую для задачи бинарной классификации.
    В случае, когда нет ни одного объекта положительного класса функция должна вызывать ValueError().

    Args:
        true_labels (np.ndarray): Массив истинных меток класса. Состоит из 0 и 1.
            1 считается меткой положительного класса.
        predicted_probas (np.ndarray): Массив предсказанных вероятностей принадлежности объекта
            к положительному классу.

    Returns:
        np.ndarray: Массив размерами (len(true_labels)+1, 2), где в каждой строчке стоит пара (precision, recall), первым элементом всегда идет (0, 1)
    """

    y = np.asarray(true_labels).astype(int).ravel()
    p = np.asarray(predicted_probas).astype(float).ravel()

    P = y.sum()
    n = y.size

    #assert y.shape == p.shape
    #assert set(y) == {0, 1} 

    if P == 0:
        raise ValueError()
    if n == 0:
        return np.array([[0.0, 1.0]], dtype=np.float64)
    


    precision_k = np.empty(n, dtype=float)
    recall_k    = np.empty(n, dtype=float)

    thresholds = np.sort(p)[::-1]

    for i in range(n):
        t = thresholds[i]
        pred_pos = (p >= t) 
        tp = np.sum(pred_pos & (y == 1))
        fp = np.sum(pred_pos & (y == 0))
        fn = P - tp 

        precision_k[i] = tp / (tp + fp)
        recall_k[i] =    tp / (tp + fn)

    
    out = np.empty((n+1, 2), dtype=np.float64)
    out[0] = (0.0, 1.0) 
    out[1:, 0] = recall_k
    out[1:, 1] = precision_k
    return out    