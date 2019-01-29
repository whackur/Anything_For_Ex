import tensorflow as tf

# Create a constant op
# This op is added as a note to the default graph
hello = tf.constant("Hello, Tensorflow!")

# start a TF Session
sess = tf.Session()

# run the op and get result
print(sess.run(hello))

# 'b' String indecates Bytes literals.