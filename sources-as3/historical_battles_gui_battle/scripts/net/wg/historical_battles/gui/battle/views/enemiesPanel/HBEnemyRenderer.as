package net.wg.historical_battles.gui.battle.views.enemiesPanel
{
   import flash.display.MovieClip;
   import flash.events.Event;
   import flash.text.TextField;
   import net.wg.data.constants.InvalidationType;
   import net.wg.data.constants.Values;
   import net.wg.gui.battle.components.BattleUIComponent;
   import net.wg.gui.battle.components.stats.playersPanel.ChatCommandItemComponent;
   import net.wg.historical_battles.gui.battle.components.HBVehicleType;
   import net.wg.historical_battles.gui.battle.constants.HB_ENEMY_TYPE;
   import net.wg.historical_battles.gui.battle.views.enemiesPanel.VO.HBEnemyInfoVO;
   import net.wg.historical_battles.gui.battle.views.playersPanel.components.healthBar.HBHealthBar;
   import net.wg.infrastructure.events.ColorSchemeEvent;
   import net.wg.infrastructure.managers.IColorSchemeManager;
   
   public class HBEnemyRenderer extends BattleUIComponent
   {
      
      private static const SIZE:String = HBVehicleType.SIZE_24;
      
      private static const CHAT_COMM_MARGIN_X:int = 27;
      
      private static const CHAT_COMM_ANIMATION_Y:int = 1;
      
      private static const CHAT_COMM_ANIMATION_HEIGHT:int = 32;
      
      private static const CHAT_COMM_ANIMATION_WIDTH:int = 186;
      
      private static const TRANSPARENT_ALPHA:Number = 0.5;
       
      
      public var hitMc:MovieClip = null;
      
      public var vehicleNameTF:TextField = null;
      
      public var vehicleType:HBVehicleType = null;
      
      public var chatCommandState:ChatCommandItemComponent = null;
      
      public var healthBar:HBHealthBar = null;
      
      public var glow:HBEnemyGlow = null;
      
      private var _data:HBEnemyInfoVO = null;
      
      private var _colorMgr:IColorSchemeManager = null;
      
      private var _isChatCommVisibilityEnabled:Boolean = false;
      
      private var _vehicleType:String = null;
      
      private var _animHelper:HBEnemyAnimHelper = null;
      
      public function HBEnemyRenderer()
      {
         super();
         this._colorMgr = App.colorSchemeMgr;
         this._colorMgr.addEventListener(ColorSchemeEvent.SCHEMAS_UPDATED,this.onColorSchemasUpdatedHandler);
      }
      
      override protected function configUI() : void
      {
         if(this.hitMc != null)
         {
            this.hitArea = this.hitMc;
         }
         this.vehicleType.color = HBVehicleType.RED;
         this.vehicleType.size = SIZE;
         this.healthBar.isEnemiesPanel = true;
         this.onColorSchemasUpdatedHandler(null);
         this.chatCommandState.setAnimationOffset(CHAT_COMM_ANIMATION_Y,CHAT_COMM_ANIMATION_HEIGHT);
         this._animHelper = new HBEnemyAnimHelper(this.vehicleType,this.glow);
      }
      
      override protected function draw() : void
      {
         if(!this._data)
         {
            return;
         }
         if(isInvalid(InvalidationType.DATA))
         {
            this.vehicleNameTF.text = this._data.vehicleName;
            this.vehicleType.vehicleType = this._data.vehicleType;
            this.healthBar.setHp(this._data.hpMax,this._data.hpCurrent);
            this.setVehicleAlpha();
            this.chatCommandState.iconOffset(this.vehicleNameTF.x + this.vehicleNameTF.width - this.vehicleNameTF.textWidth - CHAT_COMM_MARGIN_X,CHAT_COMM_ANIMATION_WIDTH);
            this.chatCommandState.visible = this._isChatCommVisibilityEnabled;
            if(this._vehicleType != this._data.vehicleType)
            {
               this._vehicleType = this._data.vehicleType;
               if(HB_ENEMY_TYPE.needAttention(this._vehicleType))
               {
                  this._animHelper.showAttention();
               }
               else
               {
                  this._animHelper.showDefault();
               }
            }
         }
      }
      
      override protected function onDispose() : void
      {
         this._colorMgr.removeEventListener(ColorSchemeEvent.SCHEMAS_UPDATED,this.onColorSchemasUpdatedHandler);
         this._colorMgr = null;
         this._animHelper.dispose();
         this._animHelper = null;
         this.hitMc = null;
         this.vehicleNameTF = null;
         this.vehicleType.dispose();
         this.vehicleType = null;
         this.chatCommandState.dispose();
         this.chatCommandState = null;
         this.healthBar.dispose();
         this.healthBar = null;
         this.glow.dispose();
         this.glow = null;
         if(this._data)
         {
            this._data.removeEventListener(Event.CHANGE,this.onDataChangeHandler);
            this._data = null;
         }
         super.onDispose();
      }
      
      public function setChatCommand(param1:String, param2:uint) : void
      {
         this.chatCommandState.setActiveChatCommand(param1,param2);
      }
      
      public function setHp(param1:int, param2:int) : void
      {
         if(!this._data)
         {
            return;
         }
         this._data.hpCurrent = param2;
         this._data.hpMax = param1;
         this.healthBar.updateHp(param1,param2);
         this.setVehicleAlpha();
      }
      
      private function setVehicleAlpha() : void
      {
         this.vehicleNameTF.alpha = this.vehicleType.alpha = Boolean(this._data.hpCurrent) ? Number(Values.DEFAULT_ALPHA) : Number(TRANSPARENT_ALPHA);
      }
      
      public function set isChatCommVisibilityEnabled(param1:Boolean) : void
      {
         if(this._isChatCommVisibilityEnabled == param1)
         {
            return;
         }
         this._isChatCommVisibilityEnabled = param1;
         this.chatCommandState.visible = this._isChatCommVisibilityEnabled;
      }
      
      public function get vehicleID() : int
      {
         return Boolean(this._data) ? int(this._data.vehicleID) : int(0);
      }
      
      public function set data(param1:Object) : void
      {
         if(this._data == param1)
         {
            return;
         }
         if(this._data)
         {
            this._data.removeEventListener(Event.CHANGE,this.onDataChangeHandler);
         }
         this._data = HBEnemyInfoVO(param1);
         if(this._data)
         {
            this._data.addEventListener(Event.CHANGE,this.onDataChangeHandler);
         }
         invalidate();
      }
      
      private function onDataChangeHandler(param1:Event) : void
      {
         invalidate();
      }
      
      private function onColorSchemasUpdatedHandler(param1:ColorSchemeEvent) : void
      {
         var _loc2_:Boolean = this._colorMgr.getIsColorBlindS();
         this.healthBar.isBlindEnabled = _loc2_;
         this.vehicleType.color = !!_loc2_ ? HBVehicleType.PURPLE : HBVehicleType.RED;
         this.glow.isBlindEnabled = _loc2_;
      }
   }
}
