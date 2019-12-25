# -*- coding:utf-8 -*-
# @time   : 2019-12-25 13:18
# @author : xulei
# @project: DesignPattern

from StatePattern.Context import Context
from StatePattern.State import StartState, StopState


if __name__ == '__main__':
    context = Context()

    startState = StartState()
    startState.doAction(context)
    print(context.getState().toString())

    stopState = StopState()
    stopState.doAction(context)
    print(context.getState().toString())
'''
Player is in start state
Start State
Player is in stop state
Stop State
'''