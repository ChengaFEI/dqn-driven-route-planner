import tensorflow as tf


class DQN:
    """Deep Q Network for the agent to learn from the environment

    Attributes:
        a_size (int): The size of the action space
        s_size (int): The size of the state space

        input (tf.placeholder): The input placeholder for the network
        input_ (tf.placeholder): The input placeholder for the network

        w1 (tf.Variable): The weight matrix for the first layer
        b1 (tf.Variable): The bias vector for the first layer
        h1_drop (tf.Variable): The hidden layer after dropout

        w2 (tf.Variable): The weight matrix for the second layer
        b2 (tf.Variable): The bias vector for the second layer
        h2_drop (tf.Variable): The hidden layer after dropout

        w3 (tf.Variable): The weight matrix for the third layer

        action (tf.Variable): The output of the network
        predict (tf.Variable): The predicted action
        target_y (tf.placeholder): The target value for the network
        a (tf.placeholder): The action placeholder for the network
        predict_onehot (tf.Variable): The predicted action in one-hot format
        float_pre (tf.Variable): The predicted action in float format

        q (tf.Variable): The Q value of the action
        error (tf.Variable): The error of the Q value
        loss (tf.Variable): The loss of the network
        optimizer (tf.Variable): The optimizer for the network
        update (tf.Variable): The update operation for the network
    """

    def __init__(self, s_size: int, a_size: int):
        self.a_size: int = a_size
        self.s_size: int = s_size
        self.structure()

    def structure(self) -> None:
        # Step 1: Create the input and output placeholder
        init = tf.glorot_normal_initializer()

        self.input = tf.placeholder(
            dtype=tf.float32,
            shape=[None, self.s_size]
        )
        self.input_ = tf.truediv(
            self.input,
            [[180.0, 180.0]]
        )

        # Step 2: Create the network layers
        self.w1 = tf.get_variable(
            shape=[self.s_size, 10],
            dtype=tf.float32,
            name='w1',
            initializer=init
        )
        self.b1 = tf.get_variable(
            shape=[10],
            dtype=tf.float32,
            name='b1'
        )
        h1 = tf.nn.relu(tf.matmul(self.input_, self.w1) + self.b1)
        self.h1_drop = tf.nn.dropout(h1, keep_prob=0.75)

        self.w2 = tf.get_variable(
            shape=[10, 6],
            dtype=tf.float32,
            name='w2',
            initializer=init
        )
        self.b2 = tf.get_variable(
            shape=[6],
            dtype=tf.float32,
            name='b2'
        )
        h2 = tf.nn.relu(tf.matmul(h1, self.w2) + self.b2)
        self.h2_drop = tf.nn.dropout(h2, keep_prob=0.75)

        self.w3 = tf.get_variable(
            shape=[6, self.a_size],
            dtype=tf.float32,
            name='w3',
            initializer=init
        )

        # Step 3: Create the loss function and optimizer
        self.action = tf.matmul(self.h2_drop, self.w3)
        self.predict = tf.argmax(input=self.action, axis=1)
        self.target_y = tf.placeholder(dtype=tf.float32, shape=[None])
        self.a = tf.placeholder(dtype=tf.int32, shape=[None])
        self.predict_onehot = tf.one_hot(
            indices=self.a,
            depth=4,
            on_value=1,
            off_value=0
        )
        self.float_pre = tf.cast(self.predict_onehot, tf.float32)

        # Step 4: Target-Net's Q value in batch
        self.q = tf.reduce_sum(
            tf.multiply(self.float_pre, self.action),
            axis=1
        )
        self.error = tf.square(self.target_y - self.q)
        self.loss = tf.reduce_mean(self.error)
        self.optimizer = tf.train.AdamOptimizer(learning_rate=0.0001)
        self.update = self.optimizer.minimize(self.loss)
