% G Major Chord
[gmajor, Fs] = audioread("gmajor.wav");
single_gmajor = gmajor(:,1); % Single channel

N = length(single_gmajor); % Number of points on the FFT
f = (0:(N-1))*(Fs/N); % Frequency
X = fft(single_gmajor); % FFT of G Major chord

figure
plot(f, abs(X));
xlim([0 2000])
title("FFT of G Major Chord")
xlabel("Frequency (Hz)")
ylabel("real(fft(gmajor))")

% F Major Chord
[fmajor, Fs] = audioread("fmajor.wav");
single_fmajor = fmajor(:,1); % Single channel

N = length(single_fmajor); % Number of points on the FFT
f = (0:(N-1))*(Fs/N); % Frequency
X = fft(single_fmajor); % FFT of G Major chord

figure
plot(f, abs(X));
xlim([0 2000])
title("FFT of F Major Chord")
xlabel("Frequency (Hz)")
ylabel("real(fft(fmajor))")

% D Minor Chord
[dminor, Fs] = audioread("dminor.wav");
single_dminor = dminor(:,1); % Single channel

N = length(single_dminor); % Number of points on the FFT
f = (0:(N-1))*(Fs/N); % Frequency
X = fft(single_dminor); % FFT of G Major chord

figure
plot(f, abs(X));
xlim([0 2000])
title("FFT of D Minor Chord")
xlabel("Frequency (Hz)")
ylabel("real(fft(dminor))")

% C Major Chord
[cmajor, Fs] = audioread("cmajor.wav");
single_cmajor = cmajor(:,1); % Single channel

N = length(single_cmajor); % Number of points on the FFT
f = (0:(N-1))*(Fs/N); % Frequency
X = fft(single_cmajor); % FFT of G Major chord

figure
plot(f, abs(X));
xlim([0 2000])
title("FFT of C Major Chord")
xlabel("Frequency (Hz)")
ylabel("real(fft(cmajor))")
