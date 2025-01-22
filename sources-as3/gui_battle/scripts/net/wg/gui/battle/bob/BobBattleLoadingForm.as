package net.wg.gui.battle.bob
{
   import flash.display.MovieClip;
   import flash.filters.DropShadowFilter;
   import flash.text.TextField;
   import net.wg.data.VO.daapi.DAAPIVehicleInfoVO;
   import net.wg.data.VO.daapi.DAAPIVehicleUserTagsVO;
   import net.wg.data.constants.Linkages;
   import net.wg.data.constants.generated.BATTLE_TYPES;
   import net.wg.gui.battle.battleloading.BaseLoadingForm;
   import net.wg.gui.battle.battleloading.data.VehiclesDataProvider;
   import net.wg.gui.battle.battleloading.interfaces.IVehiclesDataProvider;
   import net.wg.gui.battle.battleloading.renderers.BaseRendererContainer;
   import net.wg.gui.battle.battleloading.renderers.IBattleLoadingRenderer;
   import net.wg.gui.battle.battleloading.vo.VisualTipInfoVO;
   import net.wg.gui.components.controls.UILoaderAlt;
   import net.wg.gui.components.minimap.MinimapPresentation;
   import net.wg.infrastructure.events.ListDataProviderEvent;
   import net.wg.infrastructure.managers.IColorSchemeManager;
   import net.wg.utils.IClassFactory;
   import org.idmedia.as3commons.util.StringUtils;
   
   public class BobBattleLoadingForm extends BaseLoadingForm
   {
      
      private static const RENDERERS_COUNT:uint = 15;
      
      private static const LOADING_BAR_MIN:int = 0;
      
      private static const LOADING_BAR_MAX:int = 1;
      
      private static const LOADING_BAR_DEF_VALUE:int = 0;
      
      private static const RENDERER_CONTAIER_LEFT_OFFSET:int = -506;
      
      private static const RENDERER_CONTAIER_TOP_OFFSET:int = 112;
      
      private static const RENDERERS_CONTAINER_NAME:String = "container";
      
      private static const TEAM_NAME_KEY_PREFIX:String = "blogger_";
       
      
      public var team1Text:TextField;
      
      public var team2Text:TextField;
      
      public var team1Descr:TextField;
      
      public var team2Descr:TextField;
      
      public var teamBGLeft:MovieClip;
      
      public var teamBGRight:MovieClip;
      
      public var bloggerLeft:UILoaderAlt;
      
      public var bloggerRight:UILoaderAlt;
      
      private var _teamDP:VehiclesDataProvider;
      
      private var _enemyDP:VehiclesDataProvider;
      
      private var _allyRenderers:Vector.<IBattleLoadingRenderer>;
      
      private var _enemyRenderers:Vector.<IBattleLoadingRenderer>;
      
      private var _renderersContainer:BaseRendererContainer;
      
      private var _colorSchemeMgr:IColorSchemeManager;
      
      public function BobBattleLoadingForm()
      {
         this._colorSchemeMgr = App.colorSchemeMgr;
         super();
      }
      
      override public function addVehiclesInfo(param1:Boolean, param2:Vector.<DAAPIVehicleInfoVO>, param3:Vector.<Number>) : void
      {
         var _loc4_:IVehiclesDataProvider = !!param1 ? this._enemyDP : this._teamDP;
         if(_loc4_.addVehiclesInfo(param2,param3))
         {
            _loc4_.invalidate();
         }
      }
      
      override public function getMapComponent() : MinimapPresentation
      {
         return null;
      }
      
      override public function setFormDisplayData(param1:VisualTipInfoVO) : void
      {
         this.configureTip(param1.tipTitleTop,param1.tipBodyTop,param1.tipIcon);
         if(this._renderersContainer)
         {
            this._renderersContainer.dispose();
            removeChild(this._renderersContainer);
         }
         this._renderersContainer = this.getRenderersContainerInstance(param1);
         this._renderersContainer.name = RENDERERS_CONTAINER_NAME;
         this._renderersContainer.mouseEnabled = false;
         this._renderersContainer.mouseChildren = false;
         this._renderersContainer.x = RENDERER_CONTAIER_LEFT_OFFSET;
         this._renderersContainer.y = RENDERER_CONTAIER_TOP_OFFSET;
         var _loc2_:Class = this.getRendererClass(param1);
         var _loc3_:int = 0;
         while(_loc3_ < RENDERERS_COUNT)
         {
            this._allyRenderers.push(new _loc2_(this._renderersContainer,_loc3_,false));
            this._enemyRenderers.push(new _loc2_(this._renderersContainer,_loc3_,true));
            _loc3_++;
         }
         addChild(this._renderersContainer);
      }
      
      override public function setMapIcon(param1:String) : void
      {
      }
      
      override public function setPlayerStatus(param1:Boolean, param2:Number, param3:uint) : void
      {
         var _loc4_:IVehiclesDataProvider = !!param1 ? this._enemyDP : this._teamDP;
         if(_loc4_.setPlayerStatus(param2,param3))
         {
            _loc4_.invalidate();
         }
      }
      
      override public function setUserTags(param1:Boolean, param2:Vector.<DAAPIVehicleUserTagsVO>) : void
      {
         var _loc3_:IVehiclesDataProvider = !!param1 ? this._enemyDP : this._teamDP;
         if(_loc3_.setUserTags(param2))
         {
            _loc3_.invalidate();
         }
      }
      
      override public function setVehicleStatus(param1:Boolean, param2:Number, param3:uint, param4:Vector.<Number>) : void
      {
         var _loc5_:IVehiclesDataProvider = !!param1 ? this._enemyDP : this._teamDP;
         var _loc6_:Boolean = _loc5_.setVehicleStatus(param2,param3);
         _loc6_ = _loc5_.setSorting(param4) || _loc6_;
         if(_loc6_)
         {
            _loc5_.invalidate();
         }
      }
      
      override public function setVehiclesData(param1:Boolean, param2:Array, param3:Vector.<Number>) : void
      {
         var _loc4_:IVehiclesDataProvider = !!param1 ? this._enemyDP : this._teamDP;
         _loc4_.setSource(param2);
         _loc4_.setSorting(param3);
         _loc4_.invalidate();
      }
      
      override public function toString() : String
      {
         return "[WG BattleLoadingForm " + name + "]";
      }
      
      override public function updateTeamsHeaders(param1:String, param2:String) : void
      {
      }
      
      override public function updateVehiclesInfo(param1:Boolean, param2:Vector.<DAAPIVehicleInfoVO>, param3:Vector.<Number>) : void
      {
         var _loc4_:IVehiclesDataProvider = !!param1 ? this._enemyDP : this._teamDP;
         var _loc5_:Boolean = _loc4_.updateVehiclesInfo(param2);
         _loc5_ = _loc4_.setSorting(param3) || _loc5_;
         if(_loc5_)
         {
            _loc4_.invalidate();
         }
      }
      
      override public function updateWinText(param1:String) : void
      {
         winText.htmlText = param1;
      }
      
      override protected function onDispose() : void
      {
         var _loc1_:IBattleLoadingRenderer = null;
         this.teamBGLeft = null;
         this.teamBGRight = null;
         this.bloggerLeft.dispose();
         this.bloggerLeft = null;
         this.bloggerRight.dispose();
         this.bloggerRight = null;
         this.team1Text = null;
         this.team2Text = null;
         this.team1Descr = null;
         this.team2Descr = null;
         this._teamDP.removeEventListener(ListDataProviderEvent.VALIDATE_ITEMS,this.onAllyDataProviderUpdateItemHandler);
         this._teamDP.cleanUp();
         this._teamDP = null;
         this._enemyDP.removeEventListener(ListDataProviderEvent.VALIDATE_ITEMS,this.onEnemyDataProviderUpdateItemHandler);
         this._enemyDP.cleanUp();
         this._enemyDP = null;
         if(this._renderersContainer)
         {
            this._renderersContainer.dispose();
            this._renderersContainer = null;
         }
         for each(_loc1_ in this._allyRenderers)
         {
            _loc1_.dispose();
         }
         this._allyRenderers.splice(0,this._allyRenderers.length);
         this._allyRenderers = null;
         for each(_loc1_ in this._enemyRenderers)
         {
            _loc1_.dispose();
         }
         this._enemyRenderers.splice(0,this._enemyRenderers.length);
         this._enemyRenderers = null;
         super.onDispose();
      }
      
      override protected function initialize() : void
      {
         super.initialize();
         battleIcon.visible = false;
         this._teamDP = new VehiclesDataProvider();
         this._teamDP.addEventListener(ListDataProviderEvent.VALIDATE_ITEMS,this.onAllyDataProviderUpdateItemHandler);
         this._enemyDP = new VehiclesDataProvider();
         this._enemyDP.addEventListener(ListDataProviderEvent.VALIDATE_ITEMS,this.onEnemyDataProviderUpdateItemHandler);
         mapIcon.visible = false;
         loadingBar.minimum = LOADING_BAR_MIN;
         loadingBar.maximum = LOADING_BAR_MAX;
         loadingBar.value = LOADING_BAR_DEF_VALUE;
         this._allyRenderers = new Vector.<IBattleLoadingRenderer>(0);
         this._enemyRenderers = new Vector.<IBattleLoadingRenderer>(0);
         helpTip.visible = false;
         tipText.visible = false;
         this.team1Descr.text = BOB.BATTLELOADING_TEAM_HEADER;
         this.team2Descr.text = BOB.BATTLELOADING_TEAM_HEADER;
      }
      
      override protected function getBattleTypeName() : String
      {
         return BATTLE_TYPES.RANDOM;
      }
      
      public function setBloggerIds(param1:Number, param2:Number) : void
      {
         var _loc3_:String = TEAM_NAME_KEY_PREFIX + param1;
         var _loc4_:String = TEAM_NAME_KEY_PREFIX + param2;
         this.applyBloggerScheme(this.teamBGLeft,this.team1Descr,this.team1Text,_loc3_);
         this.applyBloggerScheme(this.teamBGRight,this.team2Descr,this.team2Text,_loc4_);
         this.team1Text.text = BOB.battle(_loc3_);
         this.team2Text.text = BOB.battle(_loc4_);
         this.bloggerLeft.source = RES_ICONS.getBlogger(String(param1));
         this.bloggerRight.source = RES_ICONS.getBlogger(String(param2));
      }
      
      protected function getRendererClass(param1:VisualTipInfoVO) : Class
      {
         return BobTablePlayerItemRenderer;
      }
      
      protected function getRenderersContainerInstance(param1:VisualTipInfoVO) : BaseRendererContainer
      {
         var _loc2_:IClassFactory = App.utils.classFactory;
         return _loc2_.getComponent(Linkages.BATTLE_LOADING_TABLE_RENDERERS,BaseRendererContainer);
      }
      
      private function applyBloggerScheme(param1:MovieClip, param2:TextField, param3:TextField, param4:String) : void
      {
         var _loc6_:DropShadowFilter = null;
         var _loc5_:Number = this._colorSchemeMgr.getRGB(param4);
         if(param2.filters.length)
         {
            _loc6_ = DropShadowFilter(param2.filters[0]);
            _loc6_.color = _loc5_;
         }
         if(_loc6_)
         {
            param2.filters = [_loc6_];
            param3.filters = [_loc6_];
         }
         param1.transform.colorTransform = this._colorSchemeMgr.getTransform(param4);
      }
      
      private function configureTip(param1:int, param2:int, param3:String = null) : void
      {
         var _loc4_:Boolean = StringUtils.isNotEmpty(param3);
         if(_loc4_)
         {
            helpTip.y = param1;
            tipText.y = param2;
         }
      }
      
      private function onAllyDataProviderUpdateItemHandler(param1:ListDataProviderEvent) : void
      {
         var _loc4_:int = 0;
         var _loc2_:uint = this._allyRenderers.length - 1;
         var _loc3_:Vector.<int> = Vector.<int>(param1.data);
         for each(_loc4_ in _loc3_)
         {
            if(_loc4_ <= _loc2_)
            {
               this._allyRenderers[_loc4_].setData(this._teamDP.requestItemAt(_loc4_));
            }
         }
      }
      
      private function onEnemyDataProviderUpdateItemHandler(param1:ListDataProviderEvent) : void
      {
         var _loc4_:int = 0;
         var _loc2_:uint = this._enemyRenderers.length - 1;
         var _loc3_:Vector.<int> = Vector.<int>(param1.data);
         for each(_loc4_ in _loc3_)
         {
            if(_loc4_ <= _loc2_)
            {
               this._enemyRenderers[_loc4_].setData(this._enemyDP.requestItemAt(_loc4_));
            }
         }
      }
   }
}
