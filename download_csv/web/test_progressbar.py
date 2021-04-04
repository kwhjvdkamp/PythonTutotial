from awesome_progress_bar import ProgressBar
import time

total = 1
# bar = ProgressBar(total, bar_length=50)
# Progress: |=========== 00:15 ============| 100.00% Appended

# bar = ProgressBar(total, prefix='Prefix', suffix='Suffix', use_eta=True, bar_length=70)
# # Prefix: в ‡ |==>             00:00/00:14                |   5.26% Suffix

# bar = ProgressBar(total, fill='#', use_time=False, bar_length=50, use_spinner=False)
# # Progress: |##########>                   |  33.83%

# bar = ProgressBar(total, time_format='hhh mmmin sss', bar_length=70, spinner_type='s')
# # Progress: - |=======>         00h 00min 02s                  |  16.54%

bar = ProgressBar(total, bar_length=70, spinner_type='db')
# Progress: вў€вЎ± |===========>         00:04                     |  24.81

# Bar is done
try:
    for x in range(total):
        time.sleep(0.1)
        bar.iter(' Appended')
except:
    bar.stop()

bar.wait()

print('Bar is done')