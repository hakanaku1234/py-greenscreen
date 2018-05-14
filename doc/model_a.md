model_a
=======

```
backend: tensorflow
class_name: Sequential
config:
- class_name: Dense
  config:
    activation: sigmoid
    activity_regularizer: null
    batch_input_shape: !!python/tuple [null, 2646]
    bias_constraint: null
    bias_initializer:
      class_name: Zeros
      config: {}
    bias_regularizer: null
    dtype: float32
    kernel_constraint: null
    kernel_initializer:
      class_name: VarianceScaling
      config: {distribution: uniform, mode: fan_avg, scale: 1.0, seed: null}
    kernel_regularizer: null
    name: dense_1
    trainable: true
    units: 1000
    use_bias: true
- class_name: Dense
  config:
    activation: sigmoid
    activity_regularizer: null
    bias_constraint: null
    bias_initializer:
      class_name: Zeros
      config: {}
    bias_regularizer: null
    kernel_constraint: null
    kernel_initializer:
      class_name: VarianceScaling
      config: {distribution: uniform, mode: fan_avg, scale: 1.0, seed: null}
    kernel_regularizer: null
    name: dense_2
    trainable: true
    units: 100
    use_bias: true
- class_name: Dense
  config:
    activation: sigmoid
    activity_regularizer: null
    bias_constraint: null
    bias_initializer:
      class_name: Zeros
      config: {}
    bias_regularizer: null
    kernel_constraint: null
    kernel_initializer:
      class_name: VarianceScaling
      config: {distribution: uniform, mode: fan_avg, scale: 1.0, seed: null}
    kernel_regularizer: null
    name: dense_3
    trainable: true
    units: 1
    use_bias: true
keras_version: 2.1.5
```