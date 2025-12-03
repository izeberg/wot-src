package net.wg.gui.battle.views.ribbonsPanel
{
   import fl.motion.easing.Linear;
   import flash.display.MovieClip;
   import net.wg.data.constants.generated.BATTLEATLAS;
   import net.wg.gui.battle.components.BattleAtlasSprite;
   import org.idmedia.as3commons.util.StringUtils;
   import scaleform.clik.motion.Tween;
   
   public class EfficiencyBonusAnimation extends MovieClip
   {
      
      private static const VALUE_OFFSET_X:int = 8;
      
      private static const IMAGE_FX_SCALE:Number = 1.5;
      
      private static const IMAGE_FX_DELAY:uint = 400;
      
      private static const IMAGE_FX_DURATION:uint = 300;
      
      private static const WIDTH_FROM_ATLAS:uint = 32;
       
      
      public var image:BattleAtlasSprite = null;
      
      public var imageFx:BattleAtlasSprite = null;
      
      protected var _isExtendedAnim:Boolean = true;
      
      private var _imageFxTween:Tween = null;
      
      public function EfficiencyBonusAnimation()
      {
         super();
         visible = false;
         x = VALUE_OFFSET_X;
         this.image.isSmoothingEnabled = true;
         this.imageFx.isSmoothingEnabled = true;
         this.image.visible = false;
         this.imageFx.visible = false;
         this.imageFx.isCentralize = true;
      }
      
      public final function dispose() : void
      {
         this.image = null;
         this.imageFx = null;
         if(this._imageFxTween)
         {
            this._imageFxTween.dispose();
            this._imageFxTween = null;
         }
      }
      
      public function setSettings(param1:Boolean) : void
      {
         this._isExtendedAnim = param1;
         if(this._isExtendedAnim)
         {
            this._imageFxTween = new Tween(IMAGE_FX_DURATION,this.imageFx,{
               "scaleX":1,
               "scaleY":1
            },{
               "paused":true,
               "ease":Linear.easeOut,
               "delay":IMAGE_FX_DELAY,
               "onComplete":this.onTweenComplete
            });
         }
      }
      
      public function show() : void
      {
         if(this._isExtendedAnim && visible)
         {
            this.image.visible = false;
            this.imageFx.scaleX = this.imageFx.scaleY = IMAGE_FX_SCALE;
            this.imageFx.visible = true;
            this._imageFxTween.paused = false;
         }
      }
      
      public function update(param1:String, param2:String) : void
      {
         visible = StringUtils.isNotEmpty(param1);
         if(visible)
         {
            this.image.visible = !this._isExtendedAnim;
            this.image.imageName = BATTLEATLAS.getRole32x32Icon(param2);
            if(this._isExtendedAnim)
            {
               this.imageFx.imageName = BATTLEATLAS.getRole32x32Icon(param2);
            }
         }
      }
      
      private function onTweenComplete() : void
      {
         this.image.visible = true;
         this.imageFx.visible = false;
      }
      
      public function get widthFromAtlas() : Number
      {
         return WIDTH_FROM_ATLAS;
      }
   }
}
