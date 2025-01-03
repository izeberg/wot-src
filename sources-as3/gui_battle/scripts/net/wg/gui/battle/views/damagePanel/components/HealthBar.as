package net.wg.gui.battle.views.damagePanel.components
{
   import flash.display.MovieClip;
   import net.wg.data.constants.generated.BATTLEATLAS;
   import net.wg.gui.battle.components.BattleAtlasSprite;
   import net.wg.infrastructure.base.SimpleDisposable;
   
   public class HealthBar extends SimpleDisposable
   {
      
      private static const ALERT_VISIBLE_FRAME:int = 90;
       
      
      public var alertAnim:MovieClip = null;
      
      public var shadow:BattleAtlasSprite = null;
      
      public var progressMC:MovieClip = null;
      
      private var _totalFrames:int = 0;
      
      private var _alertAnimIsPlaying:Boolean = false;
      
      public function HealthBar()
      {
         super();
         this._totalFrames = totalFrames;
         this.shadow.imageName = BATTLEATLAS.PROGRESS_SHADOW;
         this.alertAnim.image.imageName = BATTLEATLAS.PROGRESS_ALERT;
         this.progressMC.image.imageName = BATTLEATLAS.PROGRESS_BG;
         this.alertAnim.stop();
      }
      
      override protected function onDispose() : void
      {
         this.shadow = null;
         this.alertAnim = null;
         this.progressMC = null;
      }
      
      public function set progress(param1:int) : void
      {
         var _loc2_:int = 0;
         _loc2_ = 1 + this._totalFrames * (param1 * 0.01) | 0;
         gotoAndStop(_loc2_);
         var _loc3_:Boolean = _loc2_ < ALERT_VISIBLE_FRAME;
         if(_loc3_ != this._alertAnimIsPlaying)
         {
            this._alertAnimIsPlaying = _loc3_;
            if(this._alertAnimIsPlaying)
            {
               this.alertAnim.play();
            }
            else
            {
               this.alertAnim.stop();
            }
         }
      }
   }
}
