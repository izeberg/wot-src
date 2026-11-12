package net.wg.gui.components.vehicleStatus
{
   import flash.display.Sprite;
   import flash.events.Event;
   import flash.events.MouseEvent;
   import flash.text.TextField;
   import flash.text.TextLineMetrics;
   import net.wg.data.constants.Values;
   import net.wg.gui.components.controls.Image;
   import net.wg.infrastructure.base.UIComponentEx;
   import net.wg.infrastructure.events.StageSizeMangerEvent;
   import net.wg.infrastructure.managers.ITooltipMgr;
   import net.wg.utils.StageBreakPointList;
   import org.idmedia.as3commons.util.StringUtils;
   import scaleform.clik.constants.InvalidationType;
   
   public class VehicleDifficulty extends UIComponentEx
   {
      
      public static const ICON_SIZE:int = 16;
      
      public static const ICONS_COUNT:int = 3;
      
      private static const MIN_DIFFICULTY:int = 1;
      
      private static const ICONS_WIDTH:int = ICONS_COUNT * ICON_SIZE;
      
      private static const ICONS_Y_OFFSET:int = 2;
      
      private static const LABEL_GAP:int = 6;
      
      private static const LABEL_Y_OFFSET:int = 1;
      
      private static const TEXT_FIELD_GUTTER:int = 2;
      
      private static const ICON_FILLED:String = RES_ICONS.MAPS_ICONS_VEHICLEDIFFICULTY_16X16_FILLED;
      
      private static const ICON_EMPTY:String = RES_ICONS.MAPS_ICONS_VEHICLEDIFFICULTY_16X16_EMPTY;
      
      private static const TOOLTIP_BY_DIFFICULTY:Vector.<String> = new <String>[Values.EMPTY_STR,TOOLTIPS.HANGAR_VEHICLEDIFFICULTY_1,TOOLTIPS.HANGAR_VEHICLEDIFFICULTY_2,TOOLTIPS.HANGAR_VEHICLEDIFFICULTY_3];
      
      private static const LABEL_BY_DIFFICULTY:Vector.<String> = new <String>[Values.EMPTY_STR,MENU.ROLEEXP_DIFFICULTYNAME_EASY,MENU.ROLEEXP_DIFFICULTYNAME_MEDIUM,MENU.ROLEEXP_DIFFICULTYNAME_HIGH];
      
      private static const SHORT_LABEL_BY_DIFFICULTY:Vector.<String> = new <String>[Values.EMPTY_STR,MENU.ROLEEXP_DIFFICULTYNAME_SHORT_EASY,MENU.ROLEEXP_DIFFICULTYNAME_SHORT_MEDIUM,MENU.ROLEEXP_DIFFICULTYNAME_SHORT_HIGH];
       
      
      public var icon0:Image = null;
      
      public var icon1:Image = null;
      
      public var icon2:Image = null;
      
      public var label:TextField = null;
      
      public var hitMc:Sprite = null;
      
      public var difficultyBg:Sprite = null;
      
      private var _icons:Vector.<Image> = null;
      
      private var _difficulty:int = -1;
      
      private var _isCompactLabel:Boolean = false;
      
      private var _showBackground:Boolean = false;
      
      private var _toolTipMgr:ITooltipMgr;
      
      public function VehicleDifficulty()
      {
         this._toolTipMgr = App.toolTipMgr;
         super();
      }
      
      override protected function initialize() : void
      {
         super.initialize();
         visible = false;
      }
      
      override protected function configUI() : void
      {
         var _loc1_:Image = null;
         super.configUI();
         this._icons = new <Image>[this.icon0,this.icon1,this.icon2];
         for each(_loc1_ in this._icons)
         {
            _loc1_.mouseEnabled = _loc1_.mouseChildren = false;
            _loc1_.smoothing = true;
            _loc1_.addEventListener(Event.CHANGE,this.onIconChangeHandler);
         }
         this.label.mouseEnabled = false;
         if(this.difficultyBg != null)
         {
            this.difficultyBg.mouseEnabled = this.difficultyBg.mouseChildren = false;
         }
         this.updateBackground();
         mouseEnabled = true;
         mouseChildren = false;
         hitArea = this.hitMc;
         addEventListener(MouseEvent.ROLL_OVER,this.onRollOverHandler);
         addEventListener(MouseEvent.ROLL_OUT,this.onRollOutHandler);
         this._isCompactLabel = this.isCompactLabel();
         App.stageSizeMgr.addEventListener(StageSizeMangerEvent.BREAK_POINT_CHANGED,this.onBreakPointChangeHandler);
      }
      
      override protected function draw() : void
      {
         var _loc3_:int = 0;
         super.draw();
         var _loc1_:Boolean = isInvalid(InvalidationType.DATA);
         var _loc2_:Boolean = isInvalid(InvalidationType.SIZE);
         if(_loc1_)
         {
            _loc3_ = 0;
            while(_loc3_ < ICONS_COUNT)
            {
               this._icons[_loc3_].source = this.getIconSource(_loc3_);
               _loc3_++;
            }
            this.updateLabel();
         }
         if(_loc1_ || _loc2_)
         {
            this.layout();
         }
         if(_loc1_)
         {
            dispatchEvent(new Event(Event.RESIZE));
         }
      }
      
      override protected function onDispose() : void
      {
         var _loc1_:Image = null;
         App.stageSizeMgr.removeEventListener(StageSizeMangerEvent.BREAK_POINT_CHANGED,this.onBreakPointChangeHandler);
         removeEventListener(MouseEvent.ROLL_OVER,this.onRollOverHandler);
         removeEventListener(MouseEvent.ROLL_OUT,this.onRollOutHandler);
         if(this._toolTipMgr != null)
         {
            this._toolTipMgr.hide();
            this._toolTipMgr = null;
         }
         hitArea = null;
         if(this.hitMc != null)
         {
            this.hitMc.graphics.clear();
            this.hitMc = null;
         }
         if(this._icons != null)
         {
            for each(_loc1_ in this._icons)
            {
               _loc1_.removeEventListener(Event.CHANGE,this.onIconChangeHandler);
               _loc1_.dispose();
            }
            this._icons.length = 0;
            this._icons = null;
         }
         this.icon0 = null;
         this.icon1 = null;
         this.icon2 = null;
         this.label = null;
         this.difficultyBg = null;
         super.onDispose();
      }
      
      public function setDifficulty(param1:int) : void
      {
         if(this._difficulty == param1)
         {
            return;
         }
         this._difficulty = param1;
         visible = param1 >= MIN_DIFFICULTY;
         if(visible)
         {
            invalidateData();
         }
      }
      
      public function set showBackground(param1:Boolean) : void
      {
         this._showBackground = param1;
         this.updateBackground();
      }
      
      public function alignLabelTo(param1:TextField) : void
      {
         var _loc2_:int = LABEL_Y_OFFSET;
         if(param1 != null && this.label.visible)
         {
            _loc2_ += param1.getLineMetrics(0).ascent - this.label.getLineMetrics(0).ascent | 0;
         }
         this.label.y = _loc2_;
         this.updateHitArea(this.height);
         this.updateBackground();
      }
      
      override public function get width() : Number
      {
         if(this.label != null && this.label.visible)
         {
            return ICONS_WIDTH + LABEL_GAP - TEXT_FIELD_GUTTER + this.label.width;
         }
         return ICONS_WIDTH;
      }
      
      override public function get height() : Number
      {
         var _loc1_:int = this.label != null && this.label.visible ? int(this.label.y + this.label.height) : int(0);
         var _loc2_:int = this.icon0 != null ? int(this.icon0.y + ICON_SIZE) : int(ICON_SIZE);
         return Math.max(_loc2_,_loc1_);
      }
      
      private function updateLabel() : void
      {
         var _loc1_:String = this.getLabelKey();
         this.label.text = Boolean(_loc1_) ? App.utils.locale.makeString(_loc1_) : Values.EMPTY_STR;
         this.label.visible = StringUtils.isNotEmpty(this.label.text);
         if(this.label.visible)
         {
            App.utils.commons.updateTextFieldSize(this.label,true,true);
         }
      }
      
      private function layout() : void
      {
         var _loc3_:TextLineMetrics = null;
         var _loc4_:Number = NaN;
         this.label.x = ICONS_WIDTH + LABEL_GAP - TEXT_FIELD_GUTTER;
         var _loc1_:int = 0;
         if(this.label.visible)
         {
            _loc3_ = this.label.getLineMetrics(0);
            _loc4_ = TEXT_FIELD_GUTTER + (_loc3_.ascent + _loc3_.descent) / 2;
            _loc1_ = (_loc4_ - ICON_SIZE / 2 | 0) + ICONS_Y_OFFSET;
         }
         var _loc2_:int = 0;
         while(_loc2_ < ICONS_COUNT)
         {
            if(this._icons[_loc2_].ready)
            {
               this._icons[_loc2_].width = ICON_SIZE;
               this._icons[_loc2_].height = ICON_SIZE;
            }
            this._icons[_loc2_].y = _loc1_;
            _loc2_++;
         }
         this.updateHitArea(this.height);
         this.updateBackground();
      }
      
      private function updateBackground() : void
      {
         if(this.difficultyBg == null)
         {
            return;
         }
         this.difficultyBg.visible = this._showBackground;
         if(this._showBackground)
         {
            this.difficultyBg.width = this.width;
            this.difficultyBg.height = this.height;
         }
      }
      
      private function updateHitArea(param1:Number) : void
      {
         if(this.hitMc == null)
         {
            return;
         }
         this.hitMc.graphics.clear();
         this.hitMc.graphics.beginFill(0,0);
         this.hitMc.graphics.drawRect(0,0,this.width,param1);
         this.hitMc.graphics.endFill();
      }
      
      private function getLabelKey() : String
      {
         var _loc1_:Vector.<String> = !!this.isCompactLabel() ? SHORT_LABEL_BY_DIFFICULTY : LABEL_BY_DIFFICULTY;
         if(this._difficulty >= MIN_DIFFICULTY && this._difficulty < _loc1_.length)
         {
            return _loc1_[this._difficulty];
         }
         return Values.EMPTY_STR;
      }
      
      private function isCompactLabel() : Boolean
      {
         return App.stageSizeMgr.currentBreakPoint == StageBreakPointList.EXTRA_SMALL;
      }
      
      private function onBreakPointChangeHandler(param1:StageSizeMangerEvent) : void
      {
         var _loc2_:Boolean = this.isCompactLabel();
         if(_loc2_ == this._isCompactLabel)
         {
            return;
         }
         this._isCompactLabel = _loc2_;
         if(visible)
         {
            invalidateData();
         }
      }
      
      private function getIconSource(param1:int) : String
      {
         return param1 < this._difficulty ? ICON_FILLED : ICON_EMPTY;
      }
      
      private function getTooltip() : String
      {
         if(this._difficulty >= MIN_DIFFICULTY && this._difficulty < TOOLTIP_BY_DIFFICULTY.length)
         {
            return TOOLTIP_BY_DIFFICULTY[this._difficulty];
         }
         return Values.EMPTY_STR;
      }
      
      private function onIconChangeHandler(param1:Event) : void
      {
         invalidateSize();
      }
      
      private function onRollOverHandler(param1:MouseEvent) : void
      {
         var _loc2_:String = this.getTooltip();
         if(_loc2_)
         {
            this._toolTipMgr.showComplex(_loc2_);
         }
      }
      
      private function onRollOutHandler(param1:MouseEvent) : void
      {
         this._toolTipMgr.hide();
      }
   }
}
