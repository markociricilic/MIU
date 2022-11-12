% G Major Chord
[gmajor, Fs] = audioread("gmajor.wav");

N = length(gmajor); % Number of points on the FFT
f = (0:(N-1))*(Fs/N); % Frequency
X = fft(gmajor); % FFT of G Major chord

figure
plot(f, abs(X));
title("FFT of G Major Chord")
xlabel("Frequency (Hz)")
ylabel("real(fft(gmajor))")

sound(gmajor, Fs)

% F Major Chord
[fmajor, Fs] = audioread("fmajor.wav");

N = length(fmajor); % Number of points on the FFT
f = (0:(N-1))*(Fs/N); % Frequency
X = fft(fmajor); % FFT

figure
plot(f, abs(X));
title("FFT of F Major Chord")
xlabel("Frequency (Hz)")
ylabel("real(fft(fmajor))")

sound(fmajor, Fs)

% D Minor Chord
[dminor, Fs] = audioread("dminor.wav");

N = length(dminor); % Number of points for the FFT
f = (0:(N-1))*(Fs/N); % Frequency
X = fft(dminor); % FFT

figure
plot(f, abs(X));
title("FFT of D Minor Chord")
xlabel("Frequency (Hz)")
ylabel("real(fft(dminor))")

sound(dminor, Fs)

% C Major Chord
[cmajor, Fs] = audioread("cmajor.wav");

N = length(cmajor); % Number of points for the FFT
f = (0:(N-1))*(Fs/N); % Frequency
X = fft(cmajor); % FFT

figure
plot(f, abs(X));
title("FFT of C Major Chord")
xlabel("Frequency (Hz)")
ylabel("real(fft(cmajor))")

sound(cmajor, Fs)

