package net.wg.white_tiger.gui.battle.views.wtBossWidget.components
{
   import net.wg.data.constants.InvalidationType;
   import net.wg.gui.battle.components.BattleUIComponent;
   
   public class BossTankIcon extends BattleUIComponent
   {
      
      private static const FRAME_ONLINE:String = "online";
      
      private static const FRAME_OFFLINE:String = "offline";
       
      
      private var _bossType:String = "boss";
      
      private var _isShieldOnline:Boolean = false;
      
      public function BossTankIcon()
      {
         super();
      }
      
      override protected function draw() : void
      {
         var _loc1_:String = null;
         super.draw();
         if(isInvalid(InvalidationType.DATA))
         {
            _loc1_ = this._bossType + "_" + (!!this._isShieldOnline ? FRAME_ONLINE : FRAME_OFFLINE);
            if(currentFrameLabel != _loc1_)
            {
               App.utils.asserter.assertFrameExists(_loc1_,this);
               gotoAndStop(_loc1_);
            }
         }
      }
      
      public function setShieldOffline() : void
      {
         if(this._isShieldOnline)
         {
            this._isShieldOnline = false;
            invalidateData();
         }
      }
      
      public function setShieldOnline() : void
      {
         if(!this._isShieldOnline)
         {
            this._isShieldOnline = true;
            invalidateData();
         }
      }
      
      public function set bossType(param1:String) : void
      {
         if(this._bossType != param1)
         {
            this._bossType = param1;
            invalidateData();
         }
      }
   }
}
