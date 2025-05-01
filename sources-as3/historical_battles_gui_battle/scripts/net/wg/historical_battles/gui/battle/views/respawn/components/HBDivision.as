package net.wg.historical_battles.gui.battle.views.respawn.components
{
   import flash.text.TextField;
   import flash.text.TextFormat;
   import net.wg.data.constants.InvalidationType;
   import net.wg.gui.battle.components.BattleUIComponent;
   import net.wg.historical_battles.gui.battle.constants.HB_STAGE_SIZE;
   import net.wg.historical_battles.gui.battle.views.respawn.constants.HB_DIVISION_PROPS;
   import net.wg.historical_battles.gui.battle.views.respawn.data.HBDivisionVO;
   import net.wg.infrastructure.interfaces.IImage;
   import net.wg.infrastructure.interfaces.entity.IUpdatable;
   import net.wg.utils.ICommons;
   
   public class HBDivision extends BattleUIComponent implements IUpdatable
   {
       
      
      public var labelTF:TextField = null;
      
      public var nameTF:TextField = null;
      
      public var emblemIcon:IImage = null;
      
      public var lineLeft:HBLine = null;
      
      public var lineRight:HBLine = null;
      
      private var _labelTf:TextFormat = null;
      
      private var _nameTf:TextFormat = null;
      
      private var _data:HBDivisionVO = null;
      
      private var _size:uint = 0;
      
      private var _commons:ICommons;
      
      public function HBDivision()
      {
         this._commons = App.utils.commons;
         super();
      }
      
      override protected function configUI() : void
      {
         super.configUI();
         this._labelTf = this.labelTF.getTextFormat();
         this._nameTf = this.nameTF.getTextFormat();
         this.labelTF.text = HB_BATTLE.RESPAWN_DIVISION;
         this.lineLeft.setMode(HBLine.MODE_HEADER);
         this.lineRight.setMode(HBLine.MODE_HEADER);
      }
      
      override protected function draw() : void
      {
         super.draw();
         if(this._data)
         {
            if(isInvalid(InvalidationType.DATA))
            {
               this.validateData();
               invalidateSize();
            }
            if(this._size != HB_STAGE_SIZE.UNDEFINED && isInvalid(InvalidationType.SIZE))
            {
               this.validateLayout();
            }
         }
      }
      
      override protected function onDispose() : void
      {
         this.emblemIcon.dispose();
         this.emblemIcon = null;
         this.lineLeft.dispose();
         this.lineLeft = null;
         this.lineRight.dispose();
         this.lineRight = null;
         this.labelTF = null;
         this.nameTF = null;
         this._labelTf = null;
         this._nameTf = null;
         this._data = null;
         this._commons = null;
         super.onDispose();
      }
      
      public function update(param1:Object) : void
      {
         if(this._data != param1)
         {
            this._data = HBDivisionVO(param1);
            invalidateData();
         }
      }
      
      public function updateSize(param1:int) : void
      {
         if(this._size != param1)
         {
            this._size = param1;
            invalidateSize();
         }
      }
      
      private function validateData() : void
      {
         this.nameTF.text = this._data.name;
         this.emblemIcon.source = this._data.emblemSrc;
      }
      
      private function validateLayout() : void
      {
         this._labelTf.size = HB_DIVISION_PROPS.getLabelFontSize(this._size);
         this._nameTf.size = HB_DIVISION_PROPS.getNameFontSize(this._size);
         this.labelTF.setTextFormat(this._labelTf);
         this.nameTF.setTextFormat(this._nameTf);
         this._commons.updateTextFieldSize(this.labelTF);
         this._commons.updateTextFieldSize(this.nameTF);
         this.emblemIcon.scaleX = this.emblemIcon.scaleY = HB_DIVISION_PROPS.getIconsScale(this._size);
         this.emblemIcon.x = HB_DIVISION_PROPS.getEmblemX(this._size);
         this.labelTF.x = HB_DIVISION_PROPS.getLabelPos(this._size).x;
         this.labelTF.y = HB_DIVISION_PROPS.getLabelPos(this._size).y;
         this.nameTF.x = HB_DIVISION_PROPS.getNamePos(this._size).x;
         this.nameTF.y = HB_DIVISION_PROPS.getNamePos(this._size).y;
         this.lineLeft.updateSize(this._size);
         this.lineRight.updateSize(this._size);
         this.lineLeft.y = this.lineRight.y = HB_DIVISION_PROPS.getLinesY(this._size);
         this.lineRight.x = HB_DIVISION_PROPS.getNamePos(this._size).x + this.nameTF.width + HB_DIVISION_PROPS.getLineRightGap(this._size) | 0;
      }
   }
}
