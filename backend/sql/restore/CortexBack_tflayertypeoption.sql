
INSERT INTO CortexBack_tflayertypeoption (id, name, type, possible_values)
VALUES (
    1,
    'Units',
    'integer',
    '[]'
  );

INSERT INTO CortexBack_tflayertypeoption (id, name, type, possible_values)
VALUES (
    2,
    'Activation',
    'string',
    '["None (linear)", "ReLu", "Sigmoid", "Tanh", "Leaky ReLu", "Maxout", "Softmax", "SiLU (swish)", "GeLU"]'
  );

INSERT INTO CortexBack_tflayertypeoption (id, name, type, possible_values)
VALUES (
    3,
    'Filters',
    'integer',
    '[]'
  );

INSERT INTO CortexBack_tflayertypeoption (id, name, type, possible_values)
VALUES (
    4,
    'Kernel width',
    'integer',
    '[]'
  );

INSERT INTO CortexBack_tflayertypeoption (id, name, type, possible_values)
VALUES (
    5,
    'Kernel height',
    'integer',
    '[]'
  );

INSERT INTO CortexBack_tflayertypeoption (id, name, type, possible_values)
VALUES (
    6,
    'Padding',
    'string',
    '["valid", "same"]'
  );

INSERT INTO CortexBack_tflayertypeoption (id, name, type, possible_values)
VALUES (
    7,
    'Input shape timesteps',
    'integer',
    '[]'
  );

INSERT INTO CortexBack_tflayertypeoption (id, name, type, possible_values)
VALUES (
    8,
    'Input shape features',
    'integer',
    '[]'
  );

INSERT INTO CortexBack_tflayertypeoption (id, name, type, possible_values)
VALUES (
    9,
    'Return sequences',
    'boolean',
    '["true", "false"]'
  );

INSERT INTO CortexBack_tflayertypeoption (id, name, type, possible_values)
VALUES (
    10,
    'Dropout',
    'float',
    '[0, 1]'
  );

INSERT INTO CortexBack_tflayertypeoption (id, name, type, possible_values)
VALUES (
    11,
    'Pool size x',
    'integer',
    '[]'
  );

INSERT INTO CortexBack_tflayertypeoption (id, name, type, possible_values)
VALUES (
    12,
    'Pool size y',
    'integer',
    '[]'
  );

INSERT INTO CortexBack_tflayertypeoption (id, name, type, possible_values)
VALUES (
    13,
    'Horizontal stride',
    'integer',
    '[]'
  );

INSERT INTO CortexBack_tflayertypeoption (id, name, type, possible_values)
VALUES (
    14,
    'Vertical stride',
    'integer',
    '[]'
  );

INSERT INTO CortexBack_tflayertypeoption (id, name, type, possible_values)
VALUES (
    15,
    'Data format',
    'string',
    '["Channels last", "Channels first"]'
  );

INSERT INTO CortexBack_tflayertypeoption (id, name, type, possible_values)
VALUES (
    16,
    'Noise shape',
    'integer',
    '[]'
  );

INSERT INTO CortexBack_tflayertypeoption (id, name, type, possible_values)
VALUES (
    17,
    'Seed',
    'integer',
    '[]'
  );

INSERT INTO CortexBack_tflayertypeoption (id, name, type, possible_values)
VALUES (
    18,
    'Trainable',
    'boolean',
    '["true", "false"]'
  );

INSERT INTO CortexBack_tflayertypeoption (id, name, type, possible_values)
VALUES (
    19,
    'Center',
    'boolean',
    '["true", "false"]'
  );

INSERT INTO CortexBack_tflayertypeoption (id, name, type, possible_values)
VALUES (
    20,
    'Scale',
    'boolean',
    '["true", "false"]'
  );

INSERT INTO CortexBack_tflayertypeoption (id, name, type, possible_values)
VALUES (
    21,
    'Momentum',
    'float',
    '[0, 1]'
  );

INSERT INTO CortexBack_tflayertypeoption (id, name, type, possible_values)
VALUES (
    22,
    'Epsilon',
    'float',
    '[0, 1]'
  );