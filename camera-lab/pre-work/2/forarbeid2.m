I = imread('distort.jpg');

%radiell forvrengning
%juster parametrene k1 og k2 for å kompensere for linseforvrengningen 
k1 = -0.10;
k2 = 0.10;
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% parametre fra kamerakalibrering
EgenverdiMatrise = [1696.03754965799 0 0;
                   0 1696.56953872037 0;
                   1991.48045117727 1531.52752412147 1];
               
% koeffisienter for radiell forvrengning               
radiellForvrengning = [k1, k2]; 
kameraParametre = cameraParameters('IntrinsicMatrix',EgenverdiMatrise,...
                                'RadialDistortion',radiellForvrengning); 

% korrigering av radiell forvrengning
[J,nyOpprinnelse] = undistortImage(I,kameraParametre,'OutputView','full');

imshow(J);
%lagre det korrigerte bildet med koeffisientene i filnavnet
imwrite(J,['korrigert-k1_',num2str(k1),'-k2_',num2str(k2),'.jpg']);