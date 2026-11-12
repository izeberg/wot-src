package net.wg.gui.components.vehicleStatus
{
   import flash.display.Sprite;
   import flash.events.Event;
   import flash.events.MouseEvent;
   import flash.text.TextField;
   import net.wg.data.constants.Directions;
   import net.wg.data.constants.generated.TOOLTIPS_CONSTANTS;
   import net.wg.gui.components.icons.TankTypeIco;
   import net.wg.gui.components.vehicleStatus.data.VehicleStatusVO;
   import net.wg.gui.components.vehicleStatus.events.VehicleStatusEvent;
   import net.wg.infrastructure.base.UIComponentEx;
   import net.wg.infrastructure.managers.ITooltipMgr;
   import net.wg.utils.ICommons;
   import net.wg.utils.helpLayout.HelpLayoutVO;
   import org.idmedia.as3commons.util.StringUtils;
   import scaleform.clik.constants.InvalidationType;
   
   public class VehicleStatus extends UIComponentEx
   {
      
      private static const ELITE_TYPE_GAP:int = -2;
      
      private static const COMMON_TYPE_GAP:int = -12;
      
      private static const HELP_LAYOUT_ID_DELIMITER:String = "_";
      
      private static const HELP_LAYOUT_WIDTH:int = 280;
      
      private static const HELP_LAYOUT_HEIGHT:int = 65;
      
      private static const HELP_LAYOUT_HEIGHT_NO_BG:int = 47;
      
      private static const HELP_LAYOUT_NO_BG_OFFSET_Y:int = -63;
      
      private static const HELP_LAYOUT_OFFSET_Y:int = -5;
      
      private static const MESSAGE_Y:int = 38;
      
      private static const MESSAGE_Y_OFFSET:int = -6;
      
      private static const SEPARATOR_GAP:int = 8;
      
      private static const SEPARATOR_HEIGHT:int = 24;
      
      private static const DIFFICULTY_NO_ROLE_OFFSET_Y:int = 4;
       
      
      public var tankTypeIcon:TankTypeIco;
      
      public var vehicleLevel:TextField = null;
      
      public var vehicleName:TextField = null;
      
      public var message:VehicleStatusMsg = null;
      
      public var roleMessage:VehicleStatusMsg = null;
      
      public var difficulty:VehicleDifficulty = null;
      
      public var difficultySeparator:Sprite = null;
      
      private var _data:VehicleStatusVO = null;
      
      private var _vehicleStateHelpLayoutId:String = "";
      
      private var _toolTipMgr:ITooltipMgr;
      
      private var _commons:ICommons;
      
      public function VehicleStatus()
      {
         this._toolTipMgr = App.toolTipMgr;
         this._commons = App.utils.commons;
         super();
      }
      
      override protected function configUI() : void
      {
         super.configUI();
         this.tankTypeIcon.mouseEnabled = this.tankTypeIcon.mouseChildren = false;
         this.roleMessage.addEventListener(MouseEvent.ROLL_OVER,this.onRoleMessageRollOverHandler);
         this.roleMessage.addEventListener(MouseEvent.ROLL_OUT,this.onRoleMessageRollOutHandler);
         this.difficulty.addEventListener(Event.RESIZE,this.onDifficultyResizeHandler);
         this.difficultySeparator.mouseEnabled = this.difficultySeparator.mouseChildren = false;
         this.difficultySeparator.visible = false;
         if(this.difficultySeparator.height > SEPARATOR_HEIGHT)
         {
            this.difficultySeparator.height = SEPARATOR_HEIGHT;
         }
         setChildIndex(this.difficultySeparator,numChildren - 1);
      }
      
      override protected function onDispose() : void
      {
         this.roleMessage.removeEventListener(MouseEvent.ROLL_OVER,this.onRoleMessageRollOverHandler);
         this.roleMessage.removeEventListener(MouseEvent.ROLL_OUT,this.onRoleMessageRollOutHandler);
         this.difficulty.removeEventListener(Event.RESIZE,this.onDifficultyResizeHandler);
         this.roleMessage.dispose();
         this.roleMessage = null;
         this.message.dispose();
         this.message = null;
         this.tankTypeIcon.dispose();
         this.tankTypeIcon = null;
         this.difficulty.dispose();
         this.difficulty = null;
         this.difficultySeparator = null;
         this.vehicleName = null;
         this.vehicleLevel = null;
         this._data = null;
         this._toolTipMgr = null;
         this._commons = null;
         super.onDispose();
      }
      
      override protected function draw() : void
      {
         var _loc1_:String = null;
         var _loc2_:Boolean = false;
         var _loc3_:String = null;
         var _loc4_:Boolean = false;
         var _loc5_:String = null;
         var _loc6_:Boolean = false;
         var _loc7_:Boolean = false;
         var _loc8_:int = 0;
         var _loc9_:uint = 0;
         var _loc10_:int = 0;
         var _loc11_:int = 0;
         super.draw();
         if(this._data)
         {
            if(isInvalid(InvalidationType.DATA))
            {
               _loc1_ = this._data.vehicleLevel;
               _loc2_ = StringUtils.isNotEmpty(_loc1_);
               this.vehicleLevel.text = _loc1_;
               this.vehicleLevel.visible = _loc2_;
               this.vehicleName.htmlText = this._data.vehicleName;
               this.tankTypeIcon.type = this._data.tankType;
               this.tankTypeIcon.validateNow();
               _loc3_ = this._data.message;
               _loc4_ = StringUtils.isNotEmpty(_loc3_);
               this.message.visible = _loc4_;
               if(_loc4_)
               {
                  this.message.setMessage(_loc3_);
                  this.message.validateNow();
               }
               _loc5_ = this._data.roleMessage;
               _loc6_ = StringUtils.isNotEmpty(_loc5_);
               this.roleMessage.visible = _loc6_;
               if(this.roleMessage.visible)
               {
                  this.roleMessage.setMessage(_loc5_);
                  this.roleMessage.validateNow();
               }
               this.difficulty.setDifficulty(this._data.difficulty);
               this.difficulty.validateNow();
               invalidateSize();
            }
            if(isInvalid(InvalidationType.SIZE))
            {
               this._commons.updateTextFieldSize(this.vehicleName,true,false);
               _loc7_ = this.vehicleLevel.visible;
               if(_loc7_)
               {
                  this._commons.updateTextFieldSize(this.vehicleLevel,true,false);
                  this.vehicleLevel.x = 0;
               }
               _loc8_ = !!this._data.isElite ? int(ELITE_TYPE_GAP) : int(COMMON_TYPE_GAP);
               _loc9_ = !!_loc7_ ? uint(this.vehicleLevel.x + this.vehicleLevel.width) : uint(0);
               this.tankTypeIcon.x = _loc9_ + this.tankTypeIcon.width + _loc8_ ^ 0;
               this.vehicleName.x = this.tankTypeIcon.x + this.tankTypeIcon.width + _loc8_ ^ 0;
               _loc10_ = this.vehicleName.x + this.vehicleName.width >> 1;
               this.vehicleLevel.x -= _loc10_;
               this.tankTypeIcon.x -= _loc10_;
               this.vehicleName.x -= _loc10_;
               _loc11_ = MESSAGE_Y;
               if(this.roleMessage.visible || this.isDifficultyVisible)
               {
                  this.layoutRoleAndDifficulty(_loc11_);
                  _loc11_ += MESSAGE_Y + MESSAGE_Y_OFFSET;
               }
               else
               {
                  this.difficultySeparator.visible = false;
               }
               if(this.message.visible)
               {
                  this.message.x = -this.message.width >> 1;
                  this.message.y = _loc11_;
               }
               dispatchEvent(new VehicleStatusEvent(VehicleStatusEvent.RESIZE));
            }
         }
      }
      
      public function createHelpLayoutData() : HelpLayoutVO
      {
         if(StringUtils.isEmpty(this._vehicleStateHelpLayoutId))
         {
            this._vehicleStateHelpLayoutId = name + HELP_LAYOUT_ID_DELIMITER + Math.random();
         }
         var _loc1_:Boolean = this.message.visible || this.roleMessage.visible || this.isDifficultyVisible;
         var _loc2_:HelpLayoutVO = new HelpLayoutVO();
         _loc2_.x = -HELP_LAYOUT_WIDTH >> 1;
         _loc2_.y = Boolean(y + _loc1_) ? int(HELP_LAYOUT_OFFSET_Y) : int(HELP_LAYOUT_NO_BG_OFFSET_Y);
         _loc2_.width = HELP_LAYOUT_WIDTH;
         _loc2_.height = !!_loc1_ ? int(HELP_LAYOUT_HEIGHT) : int(HELP_LAYOUT_HEIGHT_NO_BG);
         _loc2_.extensibilityDirection = Directions.RIGHT;
         _loc2_.message = LOBBY_HELP.HANGAR_HEADER_VEHICLE;
         _loc2_.id = this._vehicleStateHelpLayoutId;
         _loc2_.scope = this;
         return _loc2_;
      }
      
      public function setData(param1:VehicleStatusVO) : void
      {
         if(this._data != param1 && param1 != null)
         {
            this._data = param1;
            invalidateData();
         }
      }
      
      override public function get height() : Number
      {
         var _loc1_:Number = this.vehicleName.height;
         if(this.roleMessage.visible)
         {
            _loc1_ = Math.max(_loc1_,this.roleMessage.y + this.roleMessage.height);
         }
         if(this.isDifficultyVisible)
         {
            _loc1_ = Math.max(_loc1_,this.difficulty.y + this.difficulty.height);
         }
         if(this.message.visible)
         {
            _loc1_ = Math.max(_loc1_,this.message.y + this.message.height);
         }
         return _loc1_;
      }
      
      public function get statusEndX() : int
      {
         return this.x + this.message.x + this.message.width;
      }
      
      public function get statusStartY() : int
      {
         return this.y + this.message.y;
      }
      
      private function get isDifficultyVisible() : Boolean
      {
         return this.difficulty.visible;
      }
      
      private function layoutRoleAndDifficulty(param1:int) : void
      {
         var _loc2_:Number = NaN;
         var _loc4_:Number = NaN;
         this.difficultySeparator.visible = this.roleMessage.visible && this.isDifficultyVisible;
         _loc2_ = !!this.roleMessage.visible ? Number(this.getRoleTextRight()) : Number(0);
         var _loc3_:Number = _loc2_;
         if(this.isDifficultyVisible)
         {
            _loc3_ += this.difficulty.width;
         }
         if(this.difficultySeparator.visible)
         {
            _loc3_ += this.difficultySeparator.width + SEPARATOR_GAP * 2;
         }
         _loc4_ = -_loc3_ >> 1;
         if(this.roleMessage.visible)
         {
            this.roleMessage.x = _loc4_;
            this.roleMessage.y = param1;
            _loc4_ += _loc2_;
         }
         if(this.difficultySeparator.visible)
         {
            this.difficultySeparator.x = _loc4_ + SEPARATOR_GAP;
            _loc4_ += this.difficultySeparator.width + SEPARATOR_GAP * 2;
         }
         if(this.isDifficultyVisible)
         {
            this.difficulty.x = _loc4_;
            this.difficulty.y = param1 + (!!this.roleMessage.visible ? this.roleMessage.textField.y : 0);
            this.difficulty.alignLabelTo(!!this.roleMessage.visible ? this.roleMessage.textField : null);
         }
         if(this.difficultySeparator.visible)
         {
            this.difficultySeparator.y = this.difficulty.y + (Math.max(this.roleMessage.textField.height,this.difficulty.height) - this.difficultySeparator.height >> 1);
         }
      }
      
      private function getRoleTextRight() : Number
      {
         var _loc1_:TextField = this.roleMessage.textField;
         return _loc1_.x + (_loc1_.width + _loc1_.textWidth) / 2;
      }
      
      private function onDifficultyResizeHandler(param1:Event) : void
      {
         invalidateSize();
      }
      
      private function onRoleMessageRollOverHandler(param1:MouseEvent) : void
      {
         if(this._data && this._data.roleId > 0)
         {
            this._toolTipMgr.showWulfTooltip(TOOLTIPS_CONSTANTS.VEHICLE_ROLES,this._data.vehicleCD);
         }
      }
      
      private function onRoleMessageRollOutHandler(param1:MouseEvent) : void
      {
         this._toolTipMgr.hide();
      }
   }
}
