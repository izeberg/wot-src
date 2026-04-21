package net.wg.gui.battle.views.widgetsPanel
{
   import flash.display.Sprite;
   import flash.utils.Dictionary;
   import net.wg.data.constants.InvalidationType;
   import net.wg.data.constants.generated.BATTLE_WIDGETS_CONSTS;
   import net.wg.data.constants.generated.CROSSHAIR_VIEW_ID;
   import net.wg.gui.battle.views.widgetsPanel.settings.WidgetProperties;
   import net.wg.gui.battle.views.widgetsPanel.settings.WidgetSettings;
   import net.wg.infrastructure.base.meta.IWidgetsPanelMeta;
   import net.wg.infrastructure.base.meta.impl.WidgetsPanelMeta;
   
   public class WidgetsPanel extends WidgetsPanelMeta implements IWidgetsPanelMeta
   {
      
      private static const MECHANICS_SNIPER_RIGHT_X:int = 190;
      
      private static const MECHANICS_SNIPER_RIGHT_Y:int = 190;
      
      private static const MECHANICS_ARCADE_RIGHT_X:int = 150;
      
      private static const MECHANICS_ARCADE_RIGHT_Y:int = 100;
      
      private static const MECHANICS_SNIPER_LEFT_X:int = -190;
      
      private static const MECHANICS_SNIPER_LEFT_Y:int = 190;
      
      private static const MECHANICS_ARCADE_LEFT_X:int = -150;
      
      private static const MECHANICS_ARCADE_LEFT_Y:int = 100;
      
      private static const INFO_OFFSET:int = 47;
       
      
      public var mechanicsSlotLeft:Sprite;
      
      public var mechanicsSlotRight:Sprite;
      
      public var infoSlot:Sprite;
      
      public var centralSlot:Sprite;
      
      private var _crosshairType:int = 1;
      
      private var _componentsStorage:Dictionary;
      
      private var _isPlayer:Boolean = true;
      
      private var _isReplay:Boolean = false;
      
      private var _isVisible:Boolean = true;
      
      public function WidgetsPanel()
      {
         this._componentsStorage = new Dictionary();
         super();
         this.mechanicsSlotLeft.visible = false;
         this.mechanicsSlotRight.visible = false;
         this.infoSlot.visible = false;
         this.centralSlot.visible = false;
      }
      
      override protected function draw() : void
      {
         super.draw();
         var _loc1_:BaseVehicleMechanicsWidget = null;
         if(isInvalid(InvalidationType.SIZE))
         {
            if(this._crosshairType == CROSSHAIR_VIEW_ID.ARCADE)
            {
               this.mechanicsSlotRight.x = MECHANICS_ARCADE_RIGHT_X;
               this.mechanicsSlotRight.y = MECHANICS_ARCADE_RIGHT_Y;
               this.mechanicsSlotLeft.x = MECHANICS_ARCADE_LEFT_X;
               this.mechanicsSlotLeft.y = MECHANICS_ARCADE_LEFT_Y;
            }
            else if(this._crosshairType == CROSSHAIR_VIEW_ID.SNIPER)
            {
               this.mechanicsSlotRight.x = MECHANICS_SNIPER_RIGHT_X;
               this.mechanicsSlotRight.y = MECHANICS_SNIPER_RIGHT_Y;
               this.mechanicsSlotLeft.x = MECHANICS_SNIPER_LEFT_X;
               this.mechanicsSlotLeft.y = MECHANICS_SNIPER_LEFT_Y;
            }
            this.infoSlot.x = INFO_OFFSET;
            this.infoSlot.y = INFO_OFFSET;
            for each(_loc1_ in this._componentsStorage)
            {
               _loc1_.crosshairType = this._crosshairType;
            }
         }
         if(isInvalid(InvalidationType.DATA))
         {
            for each(_loc1_ in this._componentsStorage)
            {
               _loc1_.isPlayer = this._isPlayer;
               _loc1_.isReplay = this._isReplay;
            }
         }
      }
      
      override protected function onDispose() : void
      {
         this.mechanicsSlotRight = null;
         this.mechanicsSlotLeft = null;
         this.infoSlot = null;
         this.centralSlot = null;
         App.utils.data.cleanupDynamicObject(this._componentsStorage);
         this._componentsStorage = null;
         super.onDispose();
      }
      
      public function addWidget(param1:String) : void
      {
         var _loc2_:Sprite = null;
         var _loc4_:BaseVehicleMechanicsWidget = null;
         if(BATTLE_WIDGETS_CONSTS.MECHANICS_WIDGETS_RIGHT.indexOf(param1) > -1)
         {
            _loc2_ = this.mechanicsSlotRight;
         }
         else if(BATTLE_WIDGETS_CONSTS.MECHANICS_WIDGETS_LEFT.indexOf(param1) > -1)
         {
            _loc2_ = this.mechanicsSlotLeft;
         }
         else if(BATTLE_WIDGETS_CONSTS.INFO_WIDGETS.indexOf(param1) > -1)
         {
            _loc2_ = this.infoSlot;
         }
         else if(BATTLE_WIDGETS_CONSTS.CENTRAL_WIDGETS.indexOf(param1) > -1)
         {
            _loc2_ = this.centralSlot;
         }
         else
         {
            DebugUtils.LOG_ERROR("Incorrect type of slot for " + param1 + " widget!");
            _loc2_ = this.infoSlot;
         }
         var _loc3_:WidgetProperties = WidgetSettings.instance.getProperties(param1);
         if(!_loc3_)
         {
            return;
         }
         if(!this._componentsStorage[_loc3_.alias])
         {
            _loc4_ = App.utils.classFactory.getComponent(_loc3_.linkage,_loc3_.cls);
            _loc2_.addChild(_loc4_);
            _loc2_.visible = true;
            this.registerComponent(_loc4_,_loc3_.alias);
            _loc4_.isReplay = this._isReplay;
            _loc4_.isPlayer = this._isPlayer;
            _loc4_.crosshairType = this._crosshairType;
         }
      }
      
      public function as_addWidget(param1:String) : void
      {
         this.addWidget(param1);
      }
      
      public function as_isPlayer(param1:Boolean) : void
      {
         this._isPlayer = param1;
         invalidateData();
      }
      
      public function as_isReplay(param1:Boolean) : void
      {
         this._isReplay = param1;
         invalidateData();
      }
      
      public function as_setVisible(param1:Boolean) : void
      {
         if(this._isVisible == param1)
         {
            return;
         }
         this._isVisible = param1;
         this.updateVisibility();
      }
      
      public function as_updateCrosshairType(param1:int) : void
      {
         this._crosshairType = param1;
         invalidateSize();
      }
      
      public function as_updateLayout(param1:int, param2:int) : void
      {
         this.x = param1;
         this.y = param2;
         invalidateSize();
      }
      
      override protected function updateVisibility() : void
      {
         this.visible = this._isVisible && _isCompVisible;
      }
      
      private function registerComponent(param1:BaseVehicleMechanicsWidget, param2:String) : void
      {
         this._componentsStorage[param2] = param1;
         registerFlashComponentS(param1,param2);
      }
   }
}
