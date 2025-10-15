package net.wg.gui.battle.views.rocketAcceleratorPanel
{
   import flash.display.MovieClip;
   import flash.external.ExternalInterface;
   import flash.text.TextField;
   import net.wg.data.constants.generated.COMMON_INDICATOR_CONSTS;
   import net.wg.infrastructure.base.meta.ICommonIndicatorMeta;
   import net.wg.infrastructure.base.meta.impl.CommonIndicatorMeta;
   
   public class RocketAcceleratorPanel extends CommonIndicatorMeta implements ICommonIndicatorMeta
   {
      
      private static const FRACTIONAL_FORMAT_CMD:String = "getFractionalFormat";
      
      private static const INSTANTLY_POSTFIX:String = "_instantly";
      
      private static const BALLOON_Y:int = 7;
      
      private static const BALLOON_H_FULL:int = 27;
      
      private static const OFFSET:int = 59;
       
      
      public var countTF:TextField;
      
      public var timerTF:TextField;
      
      public var progressMask:MovieClip;
      
      protected var _time:Number = -1;
      
      private var _state:String = "preparing";
      
      public function RocketAcceleratorPanel()
      {
         super();
      }
      
      override protected function configUI() : void
      {
         super.configUI();
         mouseEnabled = mouseChildren = false;
         gotoAndStop(this._state + INSTANTLY_POSTFIX);
         this.progressMask.y = BALLOON_Y;
      }
      
      override protected function onDispose() : void
      {
         this.countTF = null;
         this.timerTF = null;
         this.progressMask = null;
         super.onDispose();
      }
      
      public function as_setActiveTime(param1:Number) : void
      {
         if(this._time == param1)
         {
            return;
         }
         this._time = param1;
         var _loc2_:String = ExternalInterface.call.apply(this,[FRACTIONAL_FORMAT_CMD,param1]);
         this.timerTF.text = _loc2_;
      }
      
      public function as_setCount(param1:int) : void
      {
         this.countTF.text = param1.toString();
      }
      
      public function as_setProgress(param1:Number) : void
      {
         this.progressMask.y = BALLOON_Y - BALLOON_H_FULL * param1 | 0;
      }
      
      public function as_setState(param1:String) : void
      {
         if(param1 == this._state)
         {
            return;
         }
         if(this._state == COMMON_INDICATOR_CONSTS.DISABLE)
         {
            gotoAndStop(param1 + INSTANTLY_POSTFIX);
         }
         else
         {
            gotoAndPlay(param1);
         }
         this._state = param1;
      }
      
      public function as_setVisible(param1:Boolean) : void
      {
         _isCompVisible = param1;
         this.visible = param1;
      }
      
      public function as_updateLayout(param1:Number, param2:Number) : void
      {
         this.x = param1 + OFFSET | 0;
         this.y = param2 + OFFSET | 0;
      }
   }
}
