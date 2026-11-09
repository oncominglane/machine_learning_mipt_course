# Machine Learning: базовый курс

Материалы базового курса машинного обучения: от классических методов и оценки качества моделей до нейронных сетей, обработки последовательностей и механизма attention.

## Структура репозитория

- [`lectures/`](lectures/) — презентации лекций.
- [`seminars/`](seminars/) — ноутбуки с примерами и практическими упражнениями.
- [`tasks/`](tasks/) — домашнее и лабораторное задания.
- [`exam/`](exam/) — программа курса и материалы для подготовки к экзамену.

## Лекции

1. **[Лекция 1 — введение в машинное обучение, MLE и наивный Байес](lectures/lect01_naive_bayes_mle%23ml-basic.pdf)** — основные задачи и понятия машинного обучения, исследование данных и вероятностная классификация.  
   Основные понятия: признаки и целевая переменная, функции потерь, EDA, кодирование категориальных признаков, обучение с учителем и без учителя, метод максимального правдоподобия, теорема Байеса, наивный байесовский классификатор.

2. **[Лекция 2 — линейная регрессия](lectures/lect02_linear_regression%23ml-basic.pdf)** — построение и оценка линейных моделей регрессии.  
   Основные понятия: метод наименьших квадратов, аналитическое решение, теорема Гаусса — Маркова, мультиколлинеарность, L1- и L2-регуляризация, LASSO, Elastic Net, метрики регрессии, переобучение, разбиение выборки, кросс-валидация, утечка данных.

3. **[Лекция 3 — логистическая регрессия и метрики классификации](lectures/lect03_logistic_regression_metrics_hardware%23ml-basic.pdf)** — линейная классификация, оценка качества и вычислительное оборудование для обучения моделей.  
   Основные понятия: отступ, сигмоида, логистическая функция потерь, оценка вероятностей, One-vs-Rest и One-vs-One, матрица ошибок, accuracy, precision, recall, F-мера, ROC-AUC, Precision-Recall-кривая, CPU и GPU.

4. **[Лекция 4 — SVM, PCA и kNN](lectures/lect04_svm_pca_knn%23ml-basic.pdf)** — классификация с максимальным зазором, снижение размерности и поиск ближайших соседей.  
   Основные понятия: hinge loss, ядерный трюк, сингулярное разложение, метод главных компонент, нормализация данных, метод k ближайших соседей, взвешенный kNN, приближённый поиск соседей, HNSW и векторные базы данных.

5. **[Лекция 5 — деревья решений и бэггинг](lectures/lect05_trees_bagging%23ml-basic.pdf)** — построение деревьев и объединение моделей в ансамбли.  
   Основные понятия: жадное построение дерева, критерии разбиения, энтропия, индекс Джини, регрессионные деревья, гиперпараметры, pruning, пропуски, bootstrap, bagging, случайный лес, Isolation Forest.

6. **[Лекция 6 — бустинг, SHAP и настройка гиперпараметров](lectures/lect06_boosting_shap_optuna%23ml-basic.pdf)** — разложение ошибки и последовательное построение ансамблей.  
   Основные понятия: bias-variance-noise, градиентный бустинг, базовые модели, функции потерь, XGBoost, LightGBM, CatBoost, значения SHAP, оптимизация гиперпараметров.

7. **[Лекция 7 — нейронные сети](lectures/lect07_nerual_networks%23ml-basic.pdf)** — устройство нейронных сетей и принципы их обучения.  
   Основные понятия: линейный слой, батчи, инициализация весов, функции активации, sigmoid, tanh, ReLU, softmax, кросс-энтропия, KL-дивергенция, правило цепочки, обратное распространение ошибки, градиентная оптимизация, автоматическое дифференцирование.

10. **[Лекция 10 — рекуррентные нейронные сети](lectures/lect10_rnn%23ml-basic.pdf)** — обработка последовательностей и обучение рекуррентных моделей.  
    Основные понятия: токены, скрытое состояние, vanilla RNN, затухание и взрыв градиентов, gradient clipping, LSTM, GRU, многослойные и двунаправленные RNN, pooling.

11. **[Лекция 11 — свёрточные нейронные сети](lectures/lect11_cnn%23ml-basic.pdf)** — свёртки и архитектуры для обработки изображений.  
    Основные понятия: ядро свёртки, каналы, receptive field, stride, padding, dilation, depthwise convolution, pooling, ImageNet, LeNet, AlexNet, VGG, Inception, ResNet, residual connections, EfficientNet.

12. **[Лекция 12 — attention и Transformer](lectures/lect12_attention%23ml-basic.pdf)** — машинный перевод, механизм внимания и архитектура Transformer.  
    Основные понятия: нейронный машинный перевод, Seq2Seq, encoder-decoder, attention, self-attention, Query/Key/Value, Multi-Head Attention, positional encoding, Layer Normalization, masked attention, Transformer, BERT.

В репозитории представлены лекции 1–7 и 10–12; файлы лекций 8 и 9 отсутствуют.

## Семинарские ноутбуки

В папке [`seminars/`](seminars/) собраны практические материалы по темам курса:

- [`sem03_logreg_pytorch.ipynb`](seminars/sem03_logreg_pytorch.ipynb) и [`practice_pytorch_and_dataloaders.ipynb`](seminars/practice_pytorch_and_dataloaders.ipynb) — основы PyTorch, автоматическое дифференцирование, логистическая регрессия и загрузка данных.
- [`week0_04_SVM_practice.ipynb`](seminars/week0_04_SVM_practice.ipynb) и [`week0_04_pictures_svd.ipynb`](seminars/week0_04_pictures_svd.ipynb) — SVM и сжатие изображений с помощью SVD.
- [`practice0_05_decision_trees.ipynb`](seminars/practice0_05_decision_trees.ipynb), [`practice0_05_ensembles.ipynb`](seminars/practice0_05_ensembles.ipynb) и [`week0_06_gradient_boosting.ipynb`](seminars/week0_06_gradient_boosting.ipynb) — деревья решений, бэггинг и градиентный бустинг. [`week0_05_Cross_validation_riddle.ipynb`](seminars/week0_05_Cross_validation_riddle.ipynb) посвящён ошибке при кросс-валидации.
- [`week07_nn_from_scratch.ipynb`](seminars/week07_nn_from_scratch.ipynb) и [`week07_nn_from_scratch_practice_edition.ipynb`](seminars/week07_nn_from_scratch_practice_edition.ipynb) — реализация слоёв нейронной сети на NumPy; [`vanishing_grad_example.ipynb`](seminars/vanishing_grad_example.ipynb) — пример затухания градиентов.
- [`week09_seq2seq_rnn_practice.ipynb`](seminars/week09_seq2seq_rnn_practice.ipynb) и [версия с решением](seminars/week09_seq2seq_rnn_practice_solved.ipynb) — генерация имён с помощью RNN; [`week10_cnn_seminar.ipynb`](seminars/week10_cnn_seminar.ipynb) — свёрточные сети и классификация изображений кошек и собак.

## Практические задания

- [`tasks/hw1/`](tasks/hw1/) — домашнее задание с ноутбуками и Python-файлами для реализации kNN и построения Precision-Recall-кривой.
- [`tasks/lab1/`](tasks/lab1/) — лабораторная работа по подготовке табличных данных, обучению модели классификации и оценке её качества.
