from __future__ import absolute_import
from copy import copy
import BigWorld

class VisualScriptOverrides(BigWorld.DynamicScriptComponent):

    def updateParams(self, planDefs):
        if not self.params:
            return planDefs
        result = []
        for planDef in planDefs:
            planName = planDef['name']
            planOverrides = self.params.get(planName)
            if planOverrides:
                planDef = copy(planDef)
                oldParams = planDef.get('params', {})
                newParams = copy(oldParams)
                newParams.update(planOverrides)
                planDef['params'] = newParams
            result.append(planDef)

        return result