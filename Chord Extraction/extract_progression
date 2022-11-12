% Extracting Chord Progression

[fullprogression, Fs] = audioread("fullprogression.wav");
single_channel = fullprogression(:,1); % Stereo to mono
spectrogram(single_channel,256*20, 256*15, 256*20,Fs, 'yaxis') % Spectrogram
soundsc(fullprogression, Fs);

N = length(single_channel); % Number of points on the FFT
f = (0:(N-1))*(Fs/N); % Frequency
X = fft(single_channel); % FFT of G Major chord

figure
plot(f, abs(X));
title("FFT of Chord Progression")
xlabel("Frequency (Hz)")
ylabel("real(fft(fullprogression))")
