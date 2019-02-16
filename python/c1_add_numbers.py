import tensorflow as tf

# placeholders
x = tf.placeholder(tf.float32, name = 'x')
y = tf.placeholder(tf.float32, name = 'y')

# define the operation (graph - 1 operation)
z = tf.add(x,y, name='sum')

# create the session
session = tf.Session()

# input dict
values = {x: 5.0, y: 4.0}

summary_writer = tf.summary.FileWriter('/tmp/1', session.graph)

# run the graph (session)
# run parameters:
#   [] is an array of functionis
#   input dict
result = session.run([z], values)
print (result)
