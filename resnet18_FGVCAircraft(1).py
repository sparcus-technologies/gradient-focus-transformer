{"nbformat":4,"nbformat_minor":0,"metadata":{"colab":{"provenance":[],"machine_shape":"hm","gpuType":"A100","authorship_tag":"ABX9TyMbqICE1iemY5pjvnWMKuCO"},"kernelspec":{"name":"python3","display_name":"Python 3"},"language_info":{"name":"python"},"accelerator":"GPU"},"cells":[{"cell_type":"code","execution_count":2,"metadata":{"colab":{"base_uri":"https://localhost:8080/"},"id":"e9dnb5ituJhh","outputId":"f27db810-cb8a-4662-f21b-4ec6be5bfcf1","executionInfo":{"status":"ok","timestamp":1738735863856,"user_tz":480,"elapsed":1529038,"user":{"displayName":"Amir","userId":"01290049604318857082"}}},"outputs":[{"output_type":"stream","name":"stderr","text":["Training: 100%|██████████| 105/105 [00:15<00:00,  6.81it/s]\n","Evaluating: 100%|██████████| 105/105 [00:15<00:00,  7.00it/s]\n","/usr/local/lib/python3.11/dist-packages/sklearn/metrics/_classification.py:1565: UndefinedMetricWarning: Precision is ill-defined and being set to 0.0 in labels with no predicted samples. Use `zero_division` parameter to control this behavior.\n","  _warn_prf(average, modifier, f\"{metric.capitalize()} is\", len(result))\n"]},{"output_type":"stream","name":"stdout","text":["Epoch 1/50\n","Train Loss: 4.6085, Train Acc: 1.02%\n","Val Acc: 2.01%, Precision: 0.0192, Recall: 0.0201, F1: 0.0138\n"]},{"output_type":"stream","name":"stderr","text":["Training: 100%|██████████| 105/105 [00:15<00:00,  6.70it/s]\n","Evaluating: 100%|██████████| 105/105 [00:14<00:00,  7.02it/s]\n","/usr/local/lib/python3.11/dist-packages/sklearn/metrics/_classification.py:1565: UndefinedMetricWarning: Precision is ill-defined and being set to 0.0 in labels with no predicted samples. Use `zero_division` parameter to control this behavior.\n","  _warn_prf(average, modifier, f\"{metric.capitalize()} is\", len(result))\n"]},{"output_type":"stream","name":"stdout","text":["Epoch 2/50\n","Train Loss: 4.5197, Train Acc: 4.50%\n","Val Acc: 5.52%, Precision: 0.0523, Recall: 0.0552, F1: 0.0356\n"]},{"output_type":"stream","name":"stderr","text":["Training: 100%|██████████| 105/105 [00:15<00:00,  6.84it/s]\n","Evaluating: 100%|██████████| 105/105 [00:14<00:00,  7.01it/s]\n","/usr/local/lib/python3.11/dist-packages/sklearn/metrics/_classification.py:1565: UndefinedMetricWarning: Precision is ill-defined and being set to 0.0 in labels with no predicted samples. Use `zero_division` parameter to control this behavior.\n","  _warn_prf(average, modifier, f\"{metric.capitalize()} is\", len(result))\n"]},{"output_type":"stream","name":"stdout","text":["Epoch 3/50\n","Train Loss: 4.4050, Train Acc: 9.36%\n","Val Acc: 8.85%, Precision: 0.0849, Recall: 0.0885, F1: 0.0602\n"]},{"output_type":"stream","name":"stderr","text":["Training: 100%|██████████| 105/105 [00:15<00:00,  6.88it/s]\n","Evaluating: 100%|██████████| 105/105 [00:14<00:00,  7.12it/s]\n","/usr/local/lib/python3.11/dist-packages/sklearn/metrics/_classification.py:1565: UndefinedMetricWarning: Precision is ill-defined and being set to 0.0 in labels with no predicted samples. Use `zero_division` parameter to control this behavior.\n","  _warn_prf(average, modifier, f\"{metric.capitalize()} is\", len(result))\n"]},{"output_type":"stream","name":"stdout","text":["Epoch 4/50\n","Train Loss: 4.2257, Train Acc: 14.76%\n","Val Acc: 13.29%, Precision: 0.1468, Recall: 0.1329, F1: 0.1008\n"]},{"output_type":"stream","name":"stderr","text":["Training: 100%|██████████| 105/105 [00:15<00:00,  6.87it/s]\n","Evaluating: 100%|██████████| 105/105 [00:14<00:00,  7.12it/s]\n","/usr/local/lib/python3.11/dist-packages/sklearn/metrics/_classification.py:1565: UndefinedMetricWarning: Precision is ill-defined and being set to 0.0 in labels with no predicted samples. Use `zero_division` parameter to control this behavior.\n","  _warn_prf(average, modifier, f\"{metric.capitalize()} is\", len(result))\n"]},{"output_type":"stream","name":"stdout","text":["Epoch 5/50\n","Train Loss: 4.0028, Train Acc: 23.25%\n","Val Acc: 17.04%, Precision: 0.1850, Recall: 0.1704, F1: 0.1312\n"]},{"output_type":"stream","name":"stderr","text":["Training: 100%|██████████| 105/105 [00:15<00:00,  6.81it/s]\n","Evaluating: 100%|██████████| 105/105 [00:14<00:00,  7.07it/s]\n","/usr/local/lib/python3.11/dist-packages/sklearn/metrics/_classification.py:1565: UndefinedMetricWarning: Precision is ill-defined and being set to 0.0 in labels with no predicted samples. Use `zero_division` parameter to control this behavior.\n","  _warn_prf(average, modifier, f\"{metric.capitalize()} is\", len(result))\n"]},{"output_type":"stream","name":"stdout","text":["Epoch 6/50\n","Train Loss: 3.7836, Train Acc: 29.75%\n","Val Acc: 19.80%, Precision: 0.1860, Recall: 0.1980, F1: 0.1518\n"]},{"output_type":"stream","name":"stderr","text":["Training: 100%|██████████| 105/105 [00:15<00:00,  6.85it/s]\n","Evaluating: 100%|██████████| 105/105 [00:14<00:00,  7.01it/s]\n"]},{"output_type":"stream","name":"stdout","text":["Epoch 7/50\n","Train Loss: 3.5488, Train Acc: 34.43%\n","Val Acc: 24.15%, Precision: 0.2336, Recall: 0.2415, F1: 0.1972\n"]},{"output_type":"stream","name":"stderr","text":["Training: 100%|██████████| 105/105 [00:15<00:00,  6.89it/s]\n","Evaluating: 100%|██████████| 105/105 [00:14<00:00,  7.09it/s]\n","/usr/local/lib/python3.11/dist-packages/sklearn/metrics/_classification.py:1565: UndefinedMetricWarning: Precision is ill-defined and being set to 0.0 in labels with no predicted samples. Use `zero_division` parameter to control this behavior.\n","  _warn_prf(average, modifier, f\"{metric.capitalize()} is\", len(result))\n"]},{"output_type":"stream","name":"stdout","text":["Epoch 8/50\n","Train Loss: 3.3077, Train Acc: 40.25%\n","Val Acc: 28.02%, Precision: 0.2670, Recall: 0.2802, F1: 0.2381\n"]},{"output_type":"stream","name":"stderr","text":["Training: 100%|██████████| 105/105 [00:15<00:00,  6.86it/s]\n","Evaluating: 100%|██████████| 105/105 [00:14<00:00,  7.14it/s]\n","/usr/local/lib/python3.11/dist-packages/sklearn/metrics/_classification.py:1565: UndefinedMetricWarning: Precision is ill-defined and being set to 0.0 in labels with no predicted samples. Use `zero_division` parameter to control this behavior.\n","  _warn_prf(average, modifier, f\"{metric.capitalize()} is\", len(result))\n"]},{"output_type":"stream","name":"stdout","text":["Epoch 9/50\n","Train Loss: 3.0895, Train Acc: 43.85%\n","Val Acc: 30.99%, Precision: 0.2945, Recall: 0.3099, F1: 0.2705\n"]},{"output_type":"stream","name":"stderr","text":["Training: 100%|██████████| 105/105 [00:15<00:00,  6.79it/s]\n","Evaluating: 100%|██████████| 105/105 [00:14<00:00,  7.07it/s]\n","/usr/local/lib/python3.11/dist-packages/sklearn/metrics/_classification.py:1565: UndefinedMetricWarning: Precision is ill-defined and being set to 0.0 in labels with no predicted samples. Use `zero_division` parameter to control this behavior.\n","  _warn_prf(average, modifier, f\"{metric.capitalize()} is\", len(result))\n"]},{"output_type":"stream","name":"stdout","text":["Epoch 10/50\n","Train Loss: 2.8837, Train Acc: 47.96%\n","Val Acc: 32.91%, Precision: 0.3139, Recall: 0.3291, F1: 0.2946\n"]},{"output_type":"stream","name":"stderr","text":["Training: 100%|██████████| 105/105 [00:15<00:00,  6.77it/s]\n","Evaluating: 100%|██████████| 105/105 [00:14<00:00,  7.10it/s]\n","/usr/local/lib/python3.11/dist-packages/sklearn/metrics/_classification.py:1565: UndefinedMetricWarning: Precision is ill-defined and being set to 0.0 in labels with no predicted samples. Use `zero_division` parameter to control this behavior.\n","  _warn_prf(average, modifier, f\"{metric.capitalize()} is\", len(result))\n"]},{"output_type":"stream","name":"stdout","text":["Epoch 11/50\n","Train Loss: 2.6916, Train Acc: 52.31%\n","Val Acc: 36.06%, Precision: 0.3372, Recall: 0.3606, F1: 0.3270\n"]},{"output_type":"stream","name":"stderr","text":["Training: 100%|██████████| 105/105 [00:15<00:00,  6.91it/s]\n","Evaluating: 100%|██████████| 105/105 [00:14<00:00,  7.08it/s]\n"]},{"output_type":"stream","name":"stdout","text":["Epoch 12/50\n","Train Loss: 2.5084, Train Acc: 55.40%\n","Val Acc: 37.80%, Precision: 0.3744, Recall: 0.3780, F1: 0.3473\n"]},{"output_type":"stream","name":"stderr","text":["Training: 100%|██████████| 105/105 [00:15<00:00,  6.84it/s]\n","Evaluating: 100%|██████████| 105/105 [00:14<00:00,  7.06it/s]\n"]},{"output_type":"stream","name":"stdout","text":["Epoch 13/50\n","Train Loss: 2.3602, Train Acc: 57.71%\n","Val Acc: 39.99%, Precision: 0.3995, Recall: 0.3999, F1: 0.3717\n"]},{"output_type":"stream","name":"stderr","text":["Training: 100%|██████████| 105/105 [00:15<00:00,  6.83it/s]\n","Evaluating: 100%|██████████| 105/105 [00:14<00:00,  7.07it/s]\n"]},{"output_type":"stream","name":"stdout","text":["Epoch 14/50\n","Train Loss: 2.2141, Train Acc: 62.12%\n","Val Acc: 41.46%, Precision: 0.4166, Recall: 0.4146, F1: 0.3912\n"]},{"output_type":"stream","name":"stderr","text":["Training: 100%|██████████| 105/105 [00:15<00:00,  6.92it/s]\n","Evaluating: 100%|██████████| 105/105 [00:14<00:00,  7.14it/s]\n"]},{"output_type":"stream","name":"stdout","text":["Epoch 15/50\n","Train Loss: 2.0899, Train Acc: 64.04%\n","Val Acc: 42.66%, Precision: 0.4229, Recall: 0.4266, F1: 0.4044\n"]},{"output_type":"stream","name":"stderr","text":["Training: 100%|██████████| 105/105 [00:15<00:00,  6.74it/s]\n","Evaluating: 100%|██████████| 105/105 [00:14<00:00,  7.06it/s]\n"]},{"output_type":"stream","name":"stdout","text":["Epoch 16/50\n","Train Loss: 2.0005, Train Acc: 65.69%\n","Val Acc: 44.64%, Precision: 0.4382, Recall: 0.4464, F1: 0.4262\n"]},{"output_type":"stream","name":"stderr","text":["Training: 100%|██████████| 105/105 [00:15<00:00,  6.90it/s]\n","Evaluating: 100%|██████████| 105/105 [00:15<00:00,  6.98it/s]\n"]},{"output_type":"stream","name":"stdout","text":["Epoch 17/50\n","Train Loss: 1.8984, Train Acc: 67.97%\n","Val Acc: 45.72%, Precision: 0.4577, Recall: 0.4572, F1: 0.4415\n"]},{"output_type":"stream","name":"stderr","text":["Training: 100%|██████████| 105/105 [00:15<00:00,  6.85it/s]\n","Evaluating: 100%|██████████| 105/105 [00:14<00:00,  7.15it/s]\n"]},{"output_type":"stream","name":"stdout","text":["Epoch 18/50\n","Train Loss: 1.8278, Train Acc: 69.89%\n","Val Acc: 45.90%, Precision: 0.4616, Recall: 0.4590, F1: 0.4441\n"]},{"output_type":"stream","name":"stderr","text":["Training: 100%|██████████| 105/105 [00:15<00:00,  6.88it/s]\n","Evaluating: 100%|██████████| 105/105 [00:14<00:00,  7.13it/s]\n"]},{"output_type":"stream","name":"stdout","text":["Epoch 19/50\n","Train Loss: 1.7558, Train Acc: 71.36%\n","Val Acc: 48.18%, Precision: 0.4862, Recall: 0.4818, F1: 0.4690\n"]},{"output_type":"stream","name":"stderr","text":["Training: 100%|██████████| 105/105 [00:15<00:00,  6.89it/s]\n","Evaluating: 100%|██████████| 105/105 [00:14<00:00,  7.07it/s]\n"]},{"output_type":"stream","name":"stdout","text":["Epoch 20/50\n","Train Loss: 1.6940, Train Acc: 73.49%\n","Val Acc: 47.91%, Precision: 0.4841, Recall: 0.4791, F1: 0.4657\n"]},{"output_type":"stream","name":"stderr","text":["Training: 100%|██████████| 105/105 [00:15<00:00,  6.85it/s]\n","Evaluating: 100%|██████████| 105/105 [00:14<00:00,  7.10it/s]\n"]},{"output_type":"stream","name":"stdout","text":["Epoch 21/50\n","Train Loss: 1.6585, Train Acc: 73.52%\n","Val Acc: 48.69%, Precision: 0.4892, Recall: 0.4869, F1: 0.4745\n"]},{"output_type":"stream","name":"stderr","text":["Training: 100%|██████████| 105/105 [00:15<00:00,  6.82it/s]\n","Evaluating: 100%|██████████| 105/105 [00:14<00:00,  7.10it/s]\n"]},{"output_type":"stream","name":"stdout","text":["Epoch 22/50\n","Train Loss: 1.6239, Train Acc: 73.79%\n","Val Acc: 48.54%, Precision: 0.4868, Recall: 0.4854, F1: 0.4720\n"]},{"output_type":"stream","name":"stderr","text":["Training: 100%|██████████| 105/105 [00:15<00:00,  6.90it/s]\n","Evaluating: 100%|██████████| 105/105 [00:14<00:00,  7.06it/s]\n"]},{"output_type":"stream","name":"stdout","text":["Epoch 23/50\n","Train Loss: 1.5831, Train Acc: 75.34%\n","Val Acc: 48.87%, Precision: 0.4869, Recall: 0.4887, F1: 0.4768\n"]},{"output_type":"stream","name":"stderr","text":["Training: 100%|██████████| 105/105 [00:15<00:00,  6.88it/s]\n","Evaluating: 100%|██████████| 105/105 [00:14<00:00,  7.12it/s]\n"]},{"output_type":"stream","name":"stdout","text":["Epoch 24/50\n","Train Loss: 1.5581, Train Acc: 76.18%\n","Val Acc: 49.53%, Precision: 0.4928, Recall: 0.4953, F1: 0.4831\n"]},{"output_type":"stream","name":"stderr","text":["Training: 100%|██████████| 105/105 [00:15<00:00,  6.83it/s]\n","Evaluating: 100%|██████████| 105/105 [00:14<00:00,  7.13it/s]\n"]},{"output_type":"stream","name":"stdout","text":["Epoch 25/50\n","Train Loss: 1.5422, Train Acc: 76.42%\n","Val Acc: 49.41%, Precision: 0.4946, Recall: 0.4941, F1: 0.4832\n"]},{"output_type":"stream","name":"stderr","text":["Training: 100%|██████████| 105/105 [00:15<00:00,  6.73it/s]\n","Evaluating: 100%|██████████| 105/105 [00:14<00:00,  7.06it/s]\n"]},{"output_type":"stream","name":"stdout","text":["Epoch 26/50\n","Train Loss: 1.5306, Train Acc: 77.26%\n","Val Acc: 49.68%, Precision: 0.4979, Recall: 0.4968, F1: 0.4859\n"]},{"output_type":"stream","name":"stderr","text":["Training: 100%|██████████| 105/105 [00:15<00:00,  6.79it/s]\n","Evaluating: 100%|██████████| 105/105 [00:14<00:00,  7.06it/s]\n"]},{"output_type":"stream","name":"stdout","text":["Epoch 27/50\n","Train Loss: 1.5140, Train Acc: 77.29%\n","Val Acc: 49.74%, Precision: 0.5013, Recall: 0.4974, F1: 0.4870\n"]},{"output_type":"stream","name":"stderr","text":["Training: 100%|██████████| 105/105 [00:15<00:00,  6.80it/s]\n","Evaluating: 100%|██████████| 105/105 [00:14<00:00,  7.11it/s]\n"]},{"output_type":"stream","name":"stdout","text":["Epoch 28/50\n","Train Loss: 1.5052, Train Acc: 77.74%\n","Val Acc: 49.98%, Precision: 0.5024, Recall: 0.4998, F1: 0.4891\n"]},{"output_type":"stream","name":"stderr","text":["Training: 100%|██████████| 105/105 [00:15<00:00,  6.71it/s]\n","Evaluating: 100%|██████████| 105/105 [00:14<00:00,  7.07it/s]\n"]},{"output_type":"stream","name":"stdout","text":["Epoch 29/50\n","Train Loss: 1.5031, Train Acc: 77.47%\n","Val Acc: 50.11%, Precision: 0.5060, Recall: 0.5011, F1: 0.4900\n"]},{"output_type":"stream","name":"stderr","text":["Training: 100%|██████████| 105/105 [00:15<00:00,  6.87it/s]\n","Evaluating: 100%|██████████| 105/105 [00:14<00:00,  7.13it/s]\n"]},{"output_type":"stream","name":"stdout","text":["Epoch 30/50\n","Train Loss: 1.5096, Train Acc: 77.53%\n","Val Acc: 49.98%, Precision: 0.5002, Recall: 0.4998, F1: 0.4885\n"]},{"output_type":"stream","name":"stderr","text":["Training: 100%|██████████| 105/105 [00:15<00:00,  6.93it/s]\n","Evaluating: 100%|██████████| 105/105 [00:14<00:00,  7.03it/s]\n"]},{"output_type":"stream","name":"stdout","text":["Epoch 31/50\n","Train Loss: 1.4970, Train Acc: 77.71%\n","Val Acc: 49.92%, Precision: 0.5038, Recall: 0.4992, F1: 0.4889\n"]},{"output_type":"stream","name":"stderr","text":["Training: 100%|██████████| 105/105 [00:15<00:00,  6.92it/s]\n","Evaluating: 100%|██████████| 105/105 [00:14<00:00,  7.19it/s]\n"]},{"output_type":"stream","name":"stdout","text":["Epoch 32/50\n","Train Loss: 1.5246, Train Acc: 76.75%\n","Val Acc: 49.41%, Precision: 0.4968, Recall: 0.4941, F1: 0.4828\n"]},{"output_type":"stream","name":"stderr","text":["Training: 100%|██████████| 105/105 [00:15<00:00,  6.88it/s]\n","Evaluating: 100%|██████████| 105/105 [00:14<00:00,  7.12it/s]\n"]},{"output_type":"stream","name":"stdout","text":["Epoch 33/50\n","Train Loss: 1.4982, Train Acc: 77.68%\n","Val Acc: 50.29%, Precision: 0.5025, Recall: 0.5029, F1: 0.4915\n"]},{"output_type":"stream","name":"stderr","text":["Training: 100%|██████████| 105/105 [00:15<00:00,  6.79it/s]\n","Evaluating: 100%|██████████| 105/105 [00:14<00:00,  7.10it/s]\n"]},{"output_type":"stream","name":"stdout","text":["Epoch 34/50\n","Train Loss: 1.4987, Train Acc: 77.53%\n","Val Acc: 50.08%, Precision: 0.5054, Recall: 0.5008, F1: 0.4910\n"]},{"output_type":"stream","name":"stderr","text":["Training: 100%|██████████| 105/105 [00:15<00:00,  6.91it/s]\n","Evaluating: 100%|██████████| 105/105 [00:15<00:00,  6.97it/s]\n"]},{"output_type":"stream","name":"stdout","text":["Epoch 35/50\n","Train Loss: 1.4985, Train Acc: 77.17%\n","Val Acc: 50.05%, Precision: 0.5018, Recall: 0.5005, F1: 0.4899\n"]},{"output_type":"stream","name":"stderr","text":["Training: 100%|██████████| 105/105 [00:15<00:00,  6.93it/s]\n","Evaluating: 100%|██████████| 105/105 [00:14<00:00,  7.05it/s]\n"]},{"output_type":"stream","name":"stdout","text":["Epoch 36/50\n","Train Loss: 1.4984, Train Acc: 77.68%\n","Val Acc: 49.83%, Precision: 0.4975, Recall: 0.4983, F1: 0.4866\n"]},{"output_type":"stream","name":"stderr","text":["Training: 100%|██████████| 105/105 [00:15<00:00,  6.73it/s]\n","Evaluating: 100%|██████████| 105/105 [00:14<00:00,  7.04it/s]\n"]},{"output_type":"stream","name":"stdout","text":["Epoch 37/50\n","Train Loss: 1.4819, Train Acc: 78.25%\n","Val Acc: 50.29%, Precision: 0.5075, Recall: 0.5029, F1: 0.4929\n"]},{"output_type":"stream","name":"stderr","text":["Training: 100%|██████████| 105/105 [00:15<00:00,  6.89it/s]\n","Evaluating: 100%|██████████| 105/105 [00:14<00:00,  7.08it/s]\n"]},{"output_type":"stream","name":"stdout","text":["Epoch 38/50\n","Train Loss: 1.4615, Train Acc: 77.95%\n","Val Acc: 50.53%, Precision: 0.5044, Recall: 0.5053, F1: 0.4943\n"]},{"output_type":"stream","name":"stderr","text":["Training: 100%|██████████| 105/105 [00:15<00:00,  6.84it/s]\n","Evaluating: 100%|██████████| 105/105 [00:14<00:00,  7.06it/s]\n"]},{"output_type":"stream","name":"stdout","text":["Epoch 39/50\n","Train Loss: 1.4386, Train Acc: 77.65%\n","Val Acc: 50.41%, Precision: 0.5083, Recall: 0.5041, F1: 0.4942\n"]},{"output_type":"stream","name":"stderr","text":["Training: 100%|██████████| 105/105 [00:15<00:00,  6.89it/s]\n","Evaluating: 100%|██████████| 105/105 [00:14<00:00,  7.11it/s]\n"]},{"output_type":"stream","name":"stdout","text":["Epoch 40/50\n","Train Loss: 1.4261, Train Acc: 78.73%\n","Val Acc: 51.40%, Precision: 0.5131, Recall: 0.5140, F1: 0.5044\n"]},{"output_type":"stream","name":"stderr","text":["Training: 100%|██████████| 105/105 [00:15<00:00,  6.90it/s]\n","Evaluating: 100%|██████████| 105/105 [00:14<00:00,  7.12it/s]\n"]},{"output_type":"stream","name":"stdout","text":["Epoch 41/50\n","Train Loss: 1.3973, Train Acc: 79.24%\n","Val Acc: 51.61%, Precision: 0.5173, Recall: 0.5161, F1: 0.5077\n"]},{"output_type":"stream","name":"stderr","text":["Training: 100%|██████████| 105/105 [00:15<00:00,  6.79it/s]\n","Evaluating: 100%|██████████| 105/105 [00:14<00:00,  7.10it/s]\n"]},{"output_type":"stream","name":"stdout","text":["Epoch 42/50\n","Train Loss: 1.3653, Train Acc: 79.15%\n","Val Acc: 51.46%, Precision: 0.5174, Recall: 0.5146, F1: 0.5055\n"]},{"output_type":"stream","name":"stderr","text":["Training: 100%|██████████| 105/105 [00:15<00:00,  6.85it/s]\n","Evaluating: 100%|██████████| 105/105 [00:14<00:00,  7.14it/s]\n"]},{"output_type":"stream","name":"stdout","text":["Epoch 43/50\n","Train Loss: 1.3092, Train Acc: 80.65%\n","Val Acc: 51.79%, Precision: 0.5195, Recall: 0.5179, F1: 0.5101\n"]},{"output_type":"stream","name":"stderr","text":["Training: 100%|██████████| 105/105 [00:15<00:00,  6.95it/s]\n","Evaluating: 100%|██████████| 105/105 [00:14<00:00,  7.01it/s]\n"]},{"output_type":"stream","name":"stdout","text":["Epoch 44/50\n","Train Loss: 1.2681, Train Acc: 81.67%\n","Val Acc: 53.08%, Precision: 0.5367, Recall: 0.5308, F1: 0.5242\n"]},{"output_type":"stream","name":"stderr","text":["Training: 100%|██████████| 105/105 [00:15<00:00,  6.94it/s]\n","Evaluating: 100%|██████████| 105/105 [00:14<00:00,  7.13it/s]\n"]},{"output_type":"stream","name":"stdout","text":["Epoch 45/50\n","Train Loss: 1.2224, Train Acc: 81.34%\n","Val Acc: 53.74%, Precision: 0.5452, Recall: 0.5374, F1: 0.5311\n"]},{"output_type":"stream","name":"stderr","text":["Training: 100%|██████████| 105/105 [00:15<00:00,  6.79it/s]\n","Evaluating: 100%|██████████| 105/105 [00:14<00:00,  7.11it/s]\n"]},{"output_type":"stream","name":"stdout","text":["Epoch 46/50\n","Train Loss: 1.1649, Train Acc: 83.89%\n","Val Acc: 53.50%, Precision: 0.5387, Recall: 0.5350, F1: 0.5289\n"]},{"output_type":"stream","name":"stderr","text":["Training: 100%|██████████| 105/105 [00:15<00:00,  6.76it/s]\n","Evaluating: 100%|██████████| 105/105 [00:14<00:00,  7.09it/s]\n"]},{"output_type":"stream","name":"stdout","text":["Epoch 47/50\n","Train Loss: 1.1064, Train Acc: 84.85%\n","Val Acc: 54.07%, Precision: 0.5431, Recall: 0.5407, F1: 0.5339\n"]},{"output_type":"stream","name":"stderr","text":["Training: 100%|██████████| 105/105 [00:15<00:00,  6.79it/s]\n","Evaluating: 100%|██████████| 105/105 [00:14<00:00,  7.13it/s]\n"]},{"output_type":"stream","name":"stdout","text":["Epoch 48/50\n","Train Loss: 1.0468, Train Acc: 84.91%\n","Val Acc: 54.85%, Precision: 0.5534, Recall: 0.5485, F1: 0.5439\n"]},{"output_type":"stream","name":"stderr","text":["Training: 100%|██████████| 105/105 [00:15<00:00,  6.78it/s]\n","Evaluating: 100%|██████████| 105/105 [00:14<00:00,  7.03it/s]\n"]},{"output_type":"stream","name":"stdout","text":["Epoch 49/50\n","Train Loss: 0.9997, Train Acc: 85.15%\n","Val Acc: 55.00%, Precision: 0.5561, Recall: 0.5500, F1: 0.5460\n"]},{"output_type":"stream","name":"stderr","text":["Training: 100%|██████████| 105/105 [00:15<00:00,  6.92it/s]\n","Evaluating: 100%|██████████| 105/105 [00:14<00:00,  7.13it/s]\n","<ipython-input-2-500b453ec383>:133: FutureWarning: You are using `torch.load` with `weights_only=False` (the current default value), which uses the default pickle module implicitly. It is possible to construct malicious pickle data which will execute arbitrary code during unpickling (See https://github.com/pytorch/pytorch/blob/main/SECURITY.md#untrusted-models for more details). In a future release, the default value for `weights_only` will be flipped to `True`. This limits the functions that could be executed during unpickling. Arbitrary objects will no longer be allowed to be loaded via this mode unless they are explicitly allowlisted by the user via `torch.serialization.add_safe_globals`. We recommend you start setting `weights_only=True` for any use case where you don't have full control of the loaded file. Please open an issue on GitHub for any issues related to this experimental feature.\n","  model.load_state_dict(torch.load('best_aircraft_vit.pth'))\n"]},{"output_type":"stream","name":"stdout","text":["Epoch 50/50\n","Train Loss: 0.9241, Train Acc: 86.71%\n","Val Acc: 55.27%, Precision: 0.5558, Recall: 0.5527, F1: 0.5483\n"]},{"output_type":"stream","name":"stderr","text":["Evaluating: 100%|██████████| 105/105 [00:15<00:00,  6.97it/s]"]},{"output_type":"stream","name":"stdout","text":["\n","Test Set Results:\n","Accuracy: 56.17%\n","Precision: 0.5707\n","Recall: 0.5617\n","F1-score: 0.5588\n"]},{"output_type":"stream","name":"stderr","text":["\n"]}],"source":["import torch\n","import torch.nn as nn\n","import torch.optim as optim\n","from torch.utils.data import DataLoader\n","from torchvision import datasets, transforms\n","from torchvision.transforms import InterpolationMode\n","from timm import create_model\n","from sklearn.metrics import precision_recall_fscore_support, accuracy_score\n","import numpy as np\n","from tqdm import tqdm\n","\n","# Set random seed for reproducibility\n","torch.manual_seed(42)\n","device = torch.device(\"cuda\" if torch.cuda.is_available() else \"cpu\")\n","\n","# Define transforms\n","train_transform = transforms.Compose([\n","    transforms.Resize((224, 224), interpolation=InterpolationMode.BICUBIC),\n","    transforms.RandomHorizontalFlip(),\n","    transforms.RandomAutocontrast(),\n","    transforms.ToTensor(),\n","    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])\n","])\n","\n","test_transform = transforms.Compose([\n","    transforms.Resize((224, 224), interpolation=InterpolationMode.BICUBIC),\n","    transforms.ToTensor(),\n","    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])\n","])\n","\n","# Load FGVC-Aircraft dataset\n","train_dataset = datasets.FGVCAircraft(\n","    root='./data',\n","    split='train',\n","    download=True,\n","    transform=train_transform\n",")\n","\n","val_dataset = datasets.FGVCAircraft(\n","    root='./data',\n","    split='val',\n","    download=True,\n","    transform=test_transform\n",")\n","\n","test_dataset = datasets.FGVCAircraft(\n","    root='./data',\n","    split='test',\n","    download=True,\n","    transform=test_transform\n",")\n","\n","# Create data loaders\n","batch_size = 32\n","train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True, num_workers=4)\n","val_loader = DataLoader(val_dataset, batch_size=batch_size, shuffle=False, num_workers=4)\n","test_loader = DataLoader(test_dataset, batch_size=batch_size, shuffle=False, num_workers=4)\n","\n","# Create ViT model\n","model = create_model('resnet18', pretrained=True, num_classes=len(train_dataset.classes))\n","model = model.to(device)\n","\n","# Define loss function and optimizer\n","criterion = nn.CrossEntropyLoss()\n","optimizer = optim.AdamW(model.parameters(), lr=1e-4, weight_decay=0.05)\n","scheduler = optim.lr_scheduler.CosineAnnealingLR(optimizer, T_max=30)\n","\n","def train_epoch(model, loader, criterion, optimizer):\n","    model.train()\n","    total_loss = 0\n","    correct = 0\n","    total = 0\n","\n","    for images, targets in tqdm(loader, desc=\"Training\"):\n","        images, targets = images.to(device), targets.to(device)\n","\n","        optimizer.zero_grad()\n","        outputs = model(images)\n","        loss = criterion(outputs, targets)\n","\n","        loss.backward()\n","        optimizer.step()\n","\n","        total_loss += loss.item()\n","        _, predicted = outputs.max(1)\n","        total += targets.size(0)\n","        correct += predicted.eq(targets).sum().item()\n","\n","    return total_loss / len(loader), 100. * correct / total\n","\n","def evaluate(model, loader):\n","    model.eval()\n","    all_preds = []\n","    all_targets = []\n","\n","    with torch.no_grad():\n","        for images, targets in tqdm(loader, desc=\"Evaluating\"):\n","            images = images.to(device)\n","            outputs = model(images)\n","            _, predicted = outputs.max(1)\n","\n","            all_preds.extend(predicted.cpu().numpy())\n","            all_targets.extend(targets.numpy())\n","\n","    all_preds = np.array(all_preds)\n","    all_targets = np.array(all_targets)\n","\n","    accuracy = accuracy_score(all_targets, all_preds)\n","    precision, recall, f1, _ = precision_recall_fscore_support(all_targets, all_preds, average='weighted')\n","\n","    return accuracy, precision, recall, f1\n","\n","# Training loop\n","num_epochs = 50\n","best_val_acc = 0\n","\n","for epoch in range(num_epochs):\n","    train_loss, train_acc = train_epoch(model, train_loader, criterion, optimizer)\n","    val_acc, val_precision, val_recall, val_f1 = evaluate(model, val_loader)\n","\n","    scheduler.step()\n","\n","    print(f\"Epoch {epoch+1}/{num_epochs}\")\n","    print(f\"Train Loss: {train_loss:.4f}, Train Acc: {train_acc:.2f}%\")\n","    print(f\"Val Acc: {val_acc*100:.2f}%, Precision: {val_precision:.4f}, Recall: {val_recall:.4f}, F1: {val_f1:.4f}\")\n","\n","    # Save best model\n","    if val_acc > best_val_acc:\n","        best_val_acc = val_acc\n","        torch.save(model.state_dict(), 'best_aircraft_vit.pth')\n","\n","# Load best model and evaluate on test set\n","model.load_state_dict(torch.load('best_aircraft_vit.pth'))\n","test_acc, test_precision, test_recall, test_f1 = evaluate(model, test_loader)\n","\n","print(\"\\nTest Set Results:\")\n","print(f\"Accuracy: {test_acc*100:.2f}%\")\n","print(f\"Precision: {test_precision:.4f}\")\n","print(f\"Recall: {test_recall:.4f}\")\n","print(f\"F1-score: {test_f1:.4f}\")"]}]}