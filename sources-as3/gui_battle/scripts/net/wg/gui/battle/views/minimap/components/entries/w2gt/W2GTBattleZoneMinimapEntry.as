package net.wg.gui.battle.views.minimap.components.entries.w2gt
{
   import flash.display.CapsStyle;
   import flash.display.DisplayObject;
   import flash.display.Graphics;
   import flash.display.JointStyle;
   import flash.display.LineScaleMode;
   import flash.display.MovieClip;
   import flash.display.Sprite;
   import flash.geom.Point;
   import net.wg.data.constants.BaseTooltips;
   import net.wg.data.constants.Errors;
   import net.wg.data.constants.InvalidationType;
   import net.wg.data.managers.impl.TooltipProps;
   import net.wg.gui.battle.components.BattleUIComponent;
   import net.wg.gui.battle.views.minimap.interfaces.IHoverableEntity;
   import net.wg.infrastructure.managers.ITooltipMgr;
   
   public class W2GTBattleZoneMinimapEntry extends BattleUIComponent implements IHoverableEntity
   {
      
      private static const ARGS:String = "Args";
      
      private static const COORDINATES_STEP:int = 2;
      
      private static const MITER_LIMIT:int = 10;
      
      private static const FILL_COLOR:int = 16768409;
      
      private static const FILL_ALPHA:Number = 0;
      
      private static const OUTLINE_THICKNESS:Number = 1;
      
      private static const OUTLINE_COLOR:int = 16768409;
      
      private static const OUTLINE_ALPHA:Number = 0.9;
      
      private static const DOT_RADIUS:int = 1;
      
      private static const DOT_GAP:int = 2;
      
      private static const SLASH_DELIMETER:String = "/";
      
      private static const MIN_POINTS_FOR_ZONE:int = 6;
      
      public static const INVALID_STATE:int = InvalidationType.SYSTEM_FLAGS_BORDER << 1;
       
      
      public var iconContainer:MovieClip = null;
      
      public var placeholderBorder:Sprite = null;
      
      public var hoverMc:W2gtHover = null;
      
      private var _properties:W2gtBattleZoneProperties = null;
      
      private var _tooltipMgr:ITooltipMgr = null;
      
      private var _zoneType:String = null;
      
      private var _isTooltipShown:Boolean = false;
      
      private var _isHovered:Boolean = false;
      
      private var _zones:Array;
      
      private var _hoverAlpha:Number = 0;
      
      private var _stateAlpha:Number = 0;
      
      public function W2GTBattleZoneMinimapEntry()
      {
         this._zones = [];
         super();
         this._tooltipMgr = App.toolTipMgr;
      }
      
      override protected function onDispose() : void
      {
         this.hideTooltip();
         this._tooltipMgr = null;
         this.hoverMc.dispose();
         this.hoverMc = null;
         this._zoneType = null;
         this.placeholderBorder = null;
         this.iconContainer = null;
         this._zones.splice(0,this._zones.length);
         this._zones = null;
         this._properties = null;
         super.onDispose();
      }
      
      override protected function draw() : void
      {
         super.draw();
         if(isInvalid(InvalidationType.DATA))
         {
            this.redraw();
            invalidate(INVALID_STATE);
         }
         if(isInvalid(INVALID_STATE))
         {
            this.updateState();
         }
      }
      
      private function updateState() : void
      {
         var _loc1_:Number = !!this._isHovered ? Number(this._hoverAlpha) : Number(this._stateAlpha);
         this.hoverMc.setAlpha(_loc1_);
      }
      
      public function onRollOut(param1:Point) : void
      {
         this.hideTooltip();
         this._isHovered = false;
         invalidate(INVALID_STATE);
      }
      
      public function onRollOver(param1:Point) : void
      {
         var _loc2_:TooltipProps = null;
         if(this._zoneType != null)
         {
            _loc2_ = new TooltipProps(BaseTooltips.TYPE_INFO,0,0,0,-1,0,300);
            this._tooltipMgr.showComplex(TOOLTIPS.W2GT_ZONE + SLASH_DELIMETER + this._zoneType,_loc2_);
            this._isTooltipShown = true;
         }
         this._isHovered = true;
         invalidate(INVALID_STATE);
      }
      
      public function onClick(param1:Point) : void
      {
         this.hideTooltip();
      }
      
      public function get hitTestTarget() : DisplayObject
      {
         return this.hoverMc.fillMc;
      }
      
      public function addZoneData(... rest) : void
      {
         App.utils.asserter.assertNotNull(rest,ARGS + Errors.CANT_NULL);
         App.utils.asserter.assertNotNull(rest.length < MIN_POINTS_FOR_ZONE,ARGS + Errors.WRONG_VALUE);
         this._zones = rest;
         if(rest[0] != rest[-2] || rest[1] != rest[-1])
         {
            this._zones.push(rest[0],rest[1]);
         }
         this.hoverMc.setZones(this._zones);
         invalidateData();
      }
      
      public function clearZones() : void
      {
         this._zones.splice(0,this._zones.length);
         invalidateData();
      }
      
      public function initUI(param1:String, param2:Number) : void
      {
         this._zoneType = param1;
         this._hoverAlpha = param2;
      }
      
      public function setState(param1:Number = 0.0) : void
      {
         if(this._stateAlpha != param1)
         {
            this._stateAlpha = param1;
            invalidate(INVALID_STATE);
         }
      }
      
      public function setIcon(param1:String, param2:int, param3:int) : void
      {
         this.iconContainer.gotoAndStop(param1);
         this.iconContainer.x = param2;
         this.iconContainer.y = param3;
      }
      
      public function setProperties(param1:int = 16768409, param2:Number = 0.0, param3:String = "normal", param4:String = "solid", param5:Number = 1, param6:int = 16768409, param7:Number = 0.9, param8:Number = 1, param9:Number = 2, param10:String = "normal") : void
      {
         this._properties = new W2gtBattleZoneProperties(param1,param2,param3,param4,param5,param6,param7,param8,param9,param10);
         invalidateData();
      }
      
      private function redraw() : void
      {
         if(this._properties == null)
         {
            return;
         }
         var _loc1_:Graphics = this.placeholderBorder.graphics;
         _loc1_.clear();
         if(this._properties.isSolid)
         {
            this.redrawSolidZones(_loc1_);
         }
         else if(this._properties.isDotted)
         {
            this.redrawDottedZones(_loc1_);
         }
         this.hoverMc.setFill(this._properties.fillColor);
         _loc1_.endFill();
      }
      
      private function redrawSolidZones(param1:Graphics) : void
      {
         this.placeholderBorder.blendMode = this._properties.outlineBlendMode;
         param1.lineStyle(this._properties.outlineThickness,this._properties.outlineColor,this._properties.outlineAlpha,false,LineScaleMode.VERTICAL,CapsStyle.NONE,JointStyle.MITER,MITER_LIMIT);
         var _loc2_:int = this._zones.length;
         param1.moveTo(this._zones[0],this._zones[1]);
         var _loc3_:uint = COORDINATES_STEP;
         while(_loc3_ < _loc2_)
         {
            param1.lineTo(this._zones[_loc3_],this._zones[_loc3_ + 1]);
            _loc3_ += COORDINATES_STEP;
         }
         param1.lineTo(this._zones[0],this._zones[1]);
      }
      
      private function redrawDottedZones(param1:Graphics) : void
      {
         var _loc2_:Number = 0;
         param1.beginFill(this._properties.outlineColor,this._properties.outlineAlpha);
         param1.lineStyle(0,0,0);
         var _loc3_:int = this._zones.length;
         param1.moveTo(this._zones[0],this._zones[1]);
         var _loc4_:uint = COORDINATES_STEP;
         while(_loc4_ < _loc3_)
         {
            _loc2_ = this.drawDots(param1,this._zones[_loc4_ - 2],this._zones[_loc4_ - 1],this._zones[_loc4_],this._zones[_loc4_ + 1],_loc2_);
            _loc4_ += COORDINATES_STEP;
         }
         param1.lineTo(this._zones[0],this._zones[1]);
      }
      
      private function drawDots(param1:Graphics, param2:Number, param3:Number, param4:Number, param5:Number, param6:Number) : Number
      {
         var _loc7_:Number = Math.sqrt(Math.pow(param4 - param2,2) + Math.pow(param5 - param3,2));
         var _loc8_:Number = _loc7_ + param6;
         var _loc9_:int = _loc8_ / this._properties.dotStep;
         var _loc10_:Number = this._properties.dotStep - param6;
         if(_loc9_ == 0)
         {
            return param6 + _loc7_;
         }
         var _loc11_:Number = (param4 - param2) / _loc7_;
         var _loc12_:Number = (param5 - param3) / _loc7_;
         var _loc13_:Number = _loc11_ * this._properties.dotStep;
         var _loc14_:Number = _loc12_ * this._properties.dotStep;
         var _loc15_:Number = param2 + _loc11_ * _loc10_;
         var _loc16_:Number = param3 + _loc12_ * _loc10_;
         var _loc17_:int = 0;
         while(_loc17_ < _loc9_)
         {
            param1.drawCircle(_loc15_,_loc16_,this._properties.dotRadius);
            _loc15_ += _loc13_;
            _loc16_ += _loc14_;
            _loc17_++;
         }
         return _loc8_ % this._properties.dotStep;
      }
      
      private function hideTooltip() : void
      {
         if(this._isTooltipShown)
         {
            this._isTooltipShown = false;
            this._tooltipMgr.hide();
         }
      }
   }
}
