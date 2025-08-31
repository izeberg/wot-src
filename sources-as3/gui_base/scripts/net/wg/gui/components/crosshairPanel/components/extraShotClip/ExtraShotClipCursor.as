package net.wg.gui.components.crosshairPanel.components.extraShotClip
{
   import flash.display.MovieClip;
   import net.wg.infrastructure.interfaces.entity.IDisposable;
   
   public class ExtraShotClipCursor extends MovieClip implements IDisposable
   {
      
      public static const NORMAL_STATE_LABEL:String = "normal";
      
      public static const ACTIVE_STATE_LABEL:String = "active";
      
      public static const CRITICAL_STATE_LABEL:String = "critical";
      
      private static const SHOT_STATE_LABEL:String = "shot";
      
      private static const INSTANTLY_STATE_POSTFIX:String = "_instantly";
      
      private static const CRITICAL_STATE_START_FRAME:uint = 6;
       
      
      private var _baseDisposed:Boolean = false;
      
      private var _state:String = "normal";
      
      private var _criticalStateFrame:uint = 0;
      
      public function ExtraShotClipCursor()
      {
         super();
      }
      
      protected function onDispose() : void
      {
      }
      
      public function dispose() : void
      {
         if(this._baseDisposed)
         {
            return;
         }
         this.onDispose();
         this._baseDisposed = true;
      }
      
      public function isDisposed() : Boolean
      {
         return this._baseDisposed;
      }
      
      public function setState(param1:String, param2:Boolean = false) : void
      {
         if(this._state == param1)
         {
            return;
         }
         this._state = param1;
         if(param2 && (param1 == NORMAL_STATE_LABEL || param1 == ACTIVE_STATE_LABEL))
         {
            gotoAndStop(param1 + INSTANTLY_STATE_POSTFIX);
         }
         else if(param1 == CRITICAL_STATE_LABEL)
         {
            gotoAndPlay(this._criticalStateFrame);
         }
         else
         {
            gotoAndPlay(param1);
         }
      }
      
      public function set criticalStateFrame(param1:int) : void
      {
         this._criticalStateFrame = CRITICAL_STATE_START_FRAME + param1;
      }
      
      public function showShot() : Boolean
      {
         if(this._state == NORMAL_STATE_LABEL)
         {
            return false;
         }
         this._state = NORMAL_STATE_LABEL;
         gotoAndPlay(SHOT_STATE_LABEL);
         return true;
      }
   }
}
