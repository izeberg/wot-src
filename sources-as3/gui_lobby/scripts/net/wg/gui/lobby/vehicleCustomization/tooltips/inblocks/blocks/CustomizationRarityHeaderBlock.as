package net.wg.gui.lobby.vehicleCustomization.tooltips.inblocks.blocks
{
   import flash.text.TextField;
   import flash.text.TextFormat;
   import net.wg.data.constants.Fonts;
   import net.wg.data.constants.Values;
   import net.wg.gui.components.common.video.SimpleVideoPlayer;
   import net.wg.gui.components.controls.UILoaderAlt;
   import net.wg.gui.components.tooltips.inblocks.blocks.BaseTooltipBlock;
   import net.wg.gui.lobby.vehicleCustomization.tooltips.inblocks.data.CustomizationRarityHeaderVO;
   
   public class CustomizationRarityHeaderBlock extends BaseTooltipBlock
   {
      
      private static const VIDEO_ALPHA:Number = 0.6;
       
      
      public var textField:TextField;
      
      public var rarityTextField:TextField;
      
      public var background:UILoaderAlt;
      
      public var image:UILoaderAlt;
      
      public var rarityIcon:UILoaderAlt;
      
      public var video:SimpleVideoPlayer = null;
      
      private var _data:CustomizationRarityHeaderVO;
      
      private var _isDataApplied:Boolean = false;
      
      private var _blockWidth:int = 0;
      
      private var _rarityColorsTitle:Object;
      
      private var _rarityColorsSubTitle:Object;
      
      public function CustomizationRarityHeaderBlock()
      {
         this._rarityColorsTitle = {
            "rare":"0x80D2FD",
            "epic":"0xCB8BFE",
            "legendary":"0xE7BA85"
         };
         this._rarityColorsSubTitle = {
            "rare":"0x5A93B1",
            "epic":"0x4E3B85",
            "legendary":"0xA2825D"
         };
         super();
         this.video.isLoop = true;
         this.video.alpha = VIDEO_ALPHA;
      }
      
      override public function setBlockData(param1:Object) : void
      {
         this.clearData();
         this._data = new CustomizationRarityHeaderVO(param1);
         this._isDataApplied = false;
         invalidateBlock();
      }
      
      override public function setBlockWidth(param1:int) : void
      {
         this._blockWidth = param1;
      }
      
      protected function layout() : void
      {
         this.image.x = this._blockWidth - this.image.width >> 1;
         this.image.y = this._data.imgOffset;
      }
      
      override protected function onValidateBlock() : Boolean
      {
         if(!this._isDataApplied)
         {
            this.applyBlockData();
            return true;
         }
         this.layout();
         return false;
      }
      
      private function applyBlockData() : void
      {
         this.background.source = this._data.rarityBackground;
         this.background.autoSize = this.background.maintainAspectRatio = true;
         this.rarityIcon.source = this._data.rarityIcon;
         this.image.source = this._data.imagePath;
         var _loc1_:int = this._data.width;
         var _loc2_:int = this._data.height;
         if(_loc1_ != Values.DEFAULT_INT || _loc2_ != Values.DEFAULT_INT)
         {
            this.image.autoSize = true;
            this.image.maintainAspectRatio = false;
            if(_loc1_ != Values.DEFAULT_INT)
            {
               this.image.width = _loc1_;
            }
            if(_loc2_ != Values.DEFAULT_INT)
            {
               this.image.height = _loc2_;
            }
         }
         else
         {
            this.image.autoSize = false;
            this.image.maintainAspectRatio = true;
         }
         var _loc3_:TextFormat = this.textField.getTextFormat();
         _loc3_.color = this._rarityColorsTitle[this._data.rarity];
         _loc3_.size = 20;
         _loc3_.font = Fonts.TITLE_FONT;
         this.textField.text = this._data.title;
         this.textField.defaultTextFormat = _loc3_;
         this.textField.setTextFormat(_loc3_);
         _loc3_ = this.rarityTextField.getTextFormat();
         _loc3_.color = this._rarityColorsSubTitle[this._data.rarity];
         _loc3_.size = 18;
         _loc3_.font = Fonts.FIELD_FONT;
         this.rarityTextField.text = this._data.subTitle;
         this.rarityTextField.defaultTextFormat = _loc3_;
         this.rarityTextField.setTextFormat(_loc3_);
         this.video.source = this._data.videoSource;
         this._isDataApplied = true;
      }
      
      override protected function onDispose() : void
      {
         this.clearData();
         this.textField = null;
         this.rarityTextField = null;
         this.video.dispose();
         this.video = null;
         this.background.dispose();
         this.background = null;
         this.image.dispose();
         this.image = null;
         this.rarityIcon.dispose();
         this.rarityIcon = null;
         super.onDispose();
      }
      
      private function clearData() : void
      {
         if(this._data != null)
         {
            this._data.dispose();
            this._data = null;
         }
      }
   }
}
