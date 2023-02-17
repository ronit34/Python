-module(expo).
-export([start/1]).


start(X)->
    ToFar = 100,
    startrec(X,ToFar).
    

startrec(X,ToFar)->
    1+ taylor_series(X,ToFar,0).

taylor_series(_X,0,Current)-> Current;
taylor_series(X,ToFar,Current)->
    NewCurrent = power(X,ToFar)/fact(ToFar),
    io:format("New Current ~p~n",[NewCurrent]),
    taylor_series(X,ToFar-1,NewCurrent+Current).


fact(0)->1;
fact(N)->N *fact(N-1).

power(A,B)-> math:pow(A,B).

% ==================================================================================================

% -module(solution).
% -export([main/0]).



% main() ->
%     {N, _} = string:to_integer(string:chomp(io:get_line(""))),

%     lists:foreach(fun(NItr) ->
%         {X, _} = string:to_float(string:chomp(io:get_line(""))),
%         start(X)
%         end,
%     lists:seq(1, N)),
    
%     ok.

% start(X)->
%     ToFar = 10,
%     Value=startrec(X,ToFar),io:format("~p~n",[Value]).
    

% startrec(X,ToFar)->
%     1+ taylor_series(X,ToFar,0).

% taylor_series(X,0,Current)-> Current;
% taylor_series(X,ToFar,Current)->
%     NewCurrent = power(X,ToFar)/fact(ToFar),
%     taylor_series(X,ToFar-1,NewCurrent+Current).


% fact(0)->1;
% fact(N)->N *fact(N-1).

% power(A,B)-> math:pow(A,B).