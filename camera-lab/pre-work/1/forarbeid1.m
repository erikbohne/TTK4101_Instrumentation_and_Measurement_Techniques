% Dere skal:
%   Laste inn bildet Bayer i I
%   Finne høyde og bredde
%%%%%%%%%% Endre koden her %%%%%%%%%%%%%%%%%%%
I = imread("bayer.png");
[hoyde, bredde] = size(I);


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
fargeBilde = zeros(hoyde,bredde,3);

% Dere skal:
%   Vis gråskalabildet i figur 1
%%%%%%%%%% Skriv koden deres her %%%%%%%%%%%%%%%%%%%
figure(1);
imshow(I);

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%Hent ut fargekanalene fra bildet
%blaa kanale
fargeBilde(1:2:end,1:2:end,3) = double(I(1:2:end,1:2:end))/255;
%gronn kanal
fargeBilde(1:2:end,2:2:end,2) = double(I(1:2:end,2:2:end))/255;
%gronn kanal
fargeBilde(2:2:end,1:2:end,2) = double(I(2:2:end,1:2:end))/255;

% Dere skal:
% hente ut den røde kanalen til fargebildet
%%%%%%%%%% Skriv koden deres her %%%%%%%%%%%%%%%%%%%
% rod kanal
fargeBilde(2:2:end, 2:2:end, 1) = double(I(2:2:end, 2:2:end))/255;

%Hint: seksjon "1.5 - Fargebilder og Bayer-filter" gir god teoretisk
%bakgrunn for koden for fargekanalene
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%



% Dere skal:
%   Lagre bildet som png
%   Vis bildet
%%%%%%%%%% Skriv koden deres her %%%%%%%%%%%%%%%%%%%
figure(2);
imwrite(fargeBilde, 'rod_kanal.png');
imshow(fargeBilde);

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


% Dere skal:
%   Legg til interpolering på bildet
%   Lagre bildet som png
%   Vis bildet
%%%%%%%%%% Skriv koden deres her %%%%%%%%%%%%%%%%%%%
figure(3);
fargeBildeInterpolert = demosaic(I, 'bggr');
imshow(fargeBildeInterpolert);
imwrite(fargeBildeInterpolert, 'interpolert.png');

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%




