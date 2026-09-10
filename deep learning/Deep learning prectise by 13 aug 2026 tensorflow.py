import tensorflow as tf
print()
rsum=tf.random.normal([1000,1000])
print(rsum)
print('sum as :', tf.reduce_sum(rsum))


import tensorflow as tf
keras=tf.keras
mnist=keras.datasets.mnist

(X_train,y_train),(X_test,y_test)=mnist.load_data()
X_train,X_test=X_train/255.0, X_test/255.0

model=tf.keras.models.Sequential([
    tf.keras.layers.Flatten(input_shape=(28,28)),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(10, activation='softmax')

])



print("model.compile(optimizer= 'adam' ,    loss='sparse_categorical_crossentropy' ,      metrics=['accuracy']) :    \n" ,
       model.compile(optimizer= 'adam' ,
              loss='sparse_categorical_crossentropy' ,
              metrics=['accuracy'])
)
