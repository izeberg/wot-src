package net.wg.historical_battles.gui.battle.views.playersPanel.components
{
   import flash.display.DisplayObjectContainer;
   import flash.geom.Rectangle;
   import flash.text.TextField;
   import net.wg.data.constants.InvalidationType;
   import net.wg.data.constants.generated.BATTLEATLAS;
   import net.wg.gui.battle.components.BattleAtlasSprite;
   import net.wg.gui.battle.components.BattleUIComponent;
   import net.wg.historical_battles.gui.battle.views.playersPanel.HBPlayerRenderer;
   
   public class HBLiveCounter extends BattleUIComponent
   {
      
      private static const LIVES_ICON_AVAILABLE:Number = 1;
      
      private static const CROSS_ICON_AVAILABLE:Number = 0.5;
      
      private static const TEXT_AVAILABLE:Number = 0.7;
      
      private static const LIVES_ICON_DISABLE:Number = 0.35;
      
      private static const CROSS_ICON_DISABLE:Number = 0.35;
      
      private static const TEXT_DISABLE:Number = 0.35;
       
      
      public var livesTF:TextField = null;
      
      public var livesIconMc:BattleAtlasSprite = null;
      
      public var crossIconMc:BattleAtlasSprite = null;
      
      private var _lives:int = 0;
      
      private var _isAvailable:Boolean = false;
      
      public function HBLiveCounter()
      {
         super();
      }
      
      override protected function configUI() : void
      {
         super.configUI();
         this.livesIconMc.imageName = BATTLEATLAS.HB_LIVES;
         this.crossIconMc.imageName = BATTLEATLAS.HB_CROSS;
         this.replaceTFParent();
      }
      
      override protected function draw() : void
      {
         super.draw();
         if(isInvalid(InvalidationType.DATA))
         {
            this.livesTF.text = this._lives.toString();
         }
         if(isInvalid(InvalidationType.COLOR_SCHEME))
         {
            this.livesIconMc.alpha = !!this._isAvailable ? Number(LIVES_ICON_AVAILABLE) : Number(LIVES_ICON_DISABLE);
            this.crossIconMc.alpha = !!this._isAvailable ? Number(CROSS_ICON_AVAILABLE) : Number(CROSS_ICON_DISABLE);
            this.livesTF.alpha = !!this._isAvailable ? Number(TEXT_AVAILABLE) : Number(TEXT_DISABLE);
         }
      }
      
      override protected function onDispose() : void
      {
         var _loc1_:DisplayObjectContainer = this.livesTF.parent;
         if(_loc1_)
         {
            _loc1_.removeChild(this.livesTF);
         }
         this.livesTF = null;
         this.livesIconMc = null;
         this.crossIconMc = null;
         super.onDispose();
      }
      
      private function replaceTFParent() : void
      {
         var _loc1_:HBPlayerRenderer = HBPlayerRenderer(parent);
         var _loc2_:Rectangle = this.livesTF.getRect(_loc1_);
         this.livesTF.x = _loc2_.x;
         this.livesTF.y = _loc2_.y;
         _loc1_.addChildAt(this.livesTF,_loc1_.getChildIndex(_loc1_.vehicleDescTF));
      }
      
      public function set lives(param1:int) : void
      {
         if(this._lives == param1)
         {
            return;
         }
         this._lives = param1;
         invalidateData();
      }
      
      public function set isAvailable(param1:Boolean) : void
      {
         if(this._isAvailable == param1)
         {
            return;
         }
         this._isAvailable = param1;
         invalidate(InvalidationType.COLOR_SCHEME);
      }
   }
}
