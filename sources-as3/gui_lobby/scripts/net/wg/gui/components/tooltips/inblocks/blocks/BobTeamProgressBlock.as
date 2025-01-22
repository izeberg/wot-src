package net.wg.gui.components.tooltips.inblocks.blocks
{
   import flash.display.MovieClip;
   import flash.text.TextField;
   import flash.text.TextFieldAutoSize;
   import net.wg.gui.components.tooltips.inblocks.data.BobTeamProgressBlockVO;
   
   public class BobTeamProgressBlock extends BaseTextBlock
   {
       
      
      public var teamTF:TextField;
      
      public var progressTF:TextField;
      
      public var placeTF:TextField;
      
      public var highlightBg:MovieClip;
      
      public var like:MovieClip;
      
      private var _data:BobTeamProgressBlockVO = null;
      
      public function BobTeamProgressBlock()
      {
         super();
         this.teamTF.autoSize = TextFieldAutoSize.LEFT;
         this.progressTF.autoSize = TextFieldAutoSize.LEFT;
         this.placeTF.autoSize = TextFieldAutoSize.LEFT;
         this.highlightBg.visible = false;
      }
      
      override public function cleanUp() : void
      {
         this.clearData();
         this.teamTF.text = this.teamTF.htmlText = null;
         this.progressTF.text = this.progressTF.htmlText = null;
         this.placeTF.text = this.placeTF.htmlText = null;
         this.highlightBg.visible = this.like.visible = false;
         super.cleanUp();
      }
      
      override public function setBlockData(param1:Object) : void
      {
         this.clearData();
         this._data = new BobTeamProgressBlockVO(param1);
         invalidateBlock();
      }
      
      override public function setBlockWidth(param1:int) : void
      {
      }
      
      override protected function onValidateBlock() : Boolean
      {
         this.applyData();
         return false;
      }
      
      override protected function onDispose() : void
      {
         this.teamTF = this.progressTF = this.placeTF = null;
         this.highlightBg = null;
         this.like = null;
         this.clearData();
         super.onDispose();
      }
      
      protected function clearData() : void
      {
         if(this._data != null)
         {
            this._data.dispose();
            this._data = null;
         }
      }
      
      private function applyData() : void
      {
         this.teamTF.htmlText = this._data.team;
         this.progressTF.htmlText = this._data.progress;
         this.placeTF.htmlText = this._data.place;
         this.highlightBg.visible = this._data.isHighlighted;
         this.like.visible = !this._data.isLikeHidden && this._data.isHighlighted;
         this.like.x = this.progressTF.x + this.progressTF.textWidth;
      }
      
      override public function getHeight() : Number
      {
         return this.highlightBg.height;
      }
   }
}
