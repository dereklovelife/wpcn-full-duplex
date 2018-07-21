function [ H ] = InitChannel( k, Nt )
%UNTITLED2 Summary of this function goes here
%   Detailed explanation goes here
    H = normrnd(0, 1, [k, Nt]);
end

