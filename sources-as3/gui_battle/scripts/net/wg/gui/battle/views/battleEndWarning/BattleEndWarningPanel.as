package net.wg.gui.battle.views.battleEndWarning
{
   import flash.display.MovieClip;
   import net.wg.data.constants.Values;
   import net.wg.gui.battle.views.battleEndWarning.containers.Timer;
   import net.wg.infrastructure.base.meta.IBattleEndWarningPanelMeta;
   import net.wg.infrastructure.base.meta.impl.BattleEndWarningPanelMeta;
   
   public class BattleEndWarningPanel extends BattleEndWarningPanelMeta implements IBattleEndWarningPanelMeta
   {
      
      private static const FRAME_SHOW:String = "show";
      
      private static const FRAME_HIDE:String = "hide";
      
      private static const DELIMITER:String = ":";
      
      private static const PERMANENT_COMPONENT_VISIBLE_HEIGHT:int = 71;
       
      
      public var background:MovieClip = null;
      
      public var timer:Timer = null;
      
      private var _hideCompletedFrameScript:int = 0;
      
      private var _animInProgress:Boolean = false;
      
      private var _visible:Boolean = true;
      
      private var _innerVisible:Boolean = false;
      
      public function BattleEndWarningPanel()
      {
         super();
      }
      
      override protected function onDispose() : void
      {
         addFrameScript(this._hideCompletedFrameScript,null);
         this.background.hitArea = null;
         this.background = null;
         this.timer.hitArea = null;
         this.timer.dispose();
         this.timer = null;
         super.onDispose();
      }
      
      override protected function configUI() : void
      {
         super.configUI();
         this.innerVisible = false;
         this._hideCompletedFrameScript = totalFrames - 1;
         addFrameScript(this._hideCompletedFrameScript,this.onHideComplete);
         App.utils.commons.addEmptyHitArea(this.background);
         App.utils.commons.addEmptyHitArea(this.timer);
      }
      
      public function as_setState(param1:Boolean) : void
      {
         if(param1)
         {
            this.innerVisible = param1;
            gotoAndPlay(FRAME_SHOW);
            this.background.gotoAndPlay(FRAME_SHOW);
            this._animInProgress = true;
            this.dispatchVisibilityChange();
         }
         else
         {
            gotoAndPlay(FRAME_HIDE);
            this.background.gotoAndPlay(FRAME_HIDE);
         }
      }
      
      public function as_setTextInfo(param1:String) : void
      {
         this.timer.infoText.text = param1;
         this.innerVisible = true;
      }
      
      public function as_setTotalTime(param1:String, param2:String) : void
      {
         this.timer.timeText.text = param1 + DELIMITER + param2;
      }
      
      private function onHideComplete() : void
      {
         this.innerVisible = false;
         this._animInProgress = false;
         this.dispatchVisibilityChange();
      }
      
      private function dispatchVisibilityChange() : void
      {
         dispatchEvent(new EndWarningPanelEvent(EndWarningPanelEvent.VISIBILITY_CHANGED));
      }
      
      override public function set visible(param1:Boolean) : void
      {
         if(this._visible != param1)
         {
            this._visible = param1;
            this.updateVisible();
            this.dispatchVisibilityChange();
         }
      }
      
      override public function get visible() : Boolean
      {
         return this._visible;
      }
      
      public function get visibility() : Boolean
      {
         return Boolean(this._animInProgress && super.visible);
      }
      
      public function get panelHeight() : int
      {
         return !!this.visibility ? int(PERMANENT_COMPONENT_VISIBLE_HEIGHT) : int(Values.ZERO);
      }
      
      private function set innerVisible(param1:Boolean) : void
      {
         if(this._innerVisible != param1)
         {
            this._innerVisible = param1;
            this.updateVisible();
         }
      }
      
      private function updateVisible() : void
      {
         super.visible = this._visible && this._innerVisible;
         this.dispatchVisibilityChange();
      }
   }
}
