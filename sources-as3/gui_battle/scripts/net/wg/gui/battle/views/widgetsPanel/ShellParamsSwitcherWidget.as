package net.wg.gui.battle.views.widgetsPanel
{
   import flash.display.MovieClip;
   import net.wg.data.constants.generated.SHELL_PARAMS_SWITCHER_WIDGET_CONSTS;
   import net.wg.infrastructure.base.meta.IShellParamsSwitcherWidgetMeta;
   import net.wg.infrastructure.base.meta.impl.ShellParamsSwitcherWidgetMeta;
   
   public class ShellParamsSwitcherWidget extends ShellParamsSwitcherWidgetMeta implements IShellParamsSwitcherWidgetMeta
   {
      
      private static const NO_PARAMS_SWITCH_TYPE:String = "none";
      
      private static const INSTANT_TRANSITION_STATES:Array = [SHELL_PARAMS_SWITCHER_WIDGET_CONSTS.SWITCHING_CRIT,SHELL_PARAMS_SWITCHER_WIDGET_CONSTS.DISABLED,SHELL_PARAMS_SWITCHER_WIDGET_CONSTS.EMPTY];
       
      
      public var paramsTypeMC:MovieClip;
      
      private var _paramsType:String = "none";
      
      public function ShellParamsSwitcherWidget()
      {
         super();
      }
      
      override protected function onDispose() : void
      {
         this.paramsTypeMC = null;
         super.onDispose();
      }
      
      public function as_setParamsType(param1:String) : void
      {
         param1 = param1 || NO_PARAMS_SWITCH_TYPE;
         if(param1 == this._paramsType)
         {
            return;
         }
         this._paramsType = param1;
         this.paramsTypeMC.gotoAndStop(param1);
      }
      
      override protected function getInstantTransitionStates() : Array
      {
         return INSTANT_TRANSITION_STATES;
      }
      
      override protected function getInitialState() : String
      {
         return SHELL_PARAMS_SWITCHER_WIDGET_CONSTS.EMPTY;
      }
      
      override protected function getHotKeyVisibility() : Boolean
      {
         var _loc1_:Boolean = super.getHotKeyVisibility();
         return Boolean(_loc1_ && (state == SHELL_PARAMS_SWITCHER_WIDGET_CONSTS.READY || state == SHELL_PARAMS_SWITCHER_WIDGET_CONSTS.ACTIVE));
      }
   }
}
